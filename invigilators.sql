-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema invigilators
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema invigilators
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `invigilators` DEFAULT CHARACTER SET utf8 ;
USE `invigilators` ;

-- -----------------------------------------------------
-- Table `invigilators`.`staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `invigilators`.`staff` (
  `staff_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `faculty` VARCHAR(255) NOT NULL,
  `fname` VARCHAR(255) NOT NULL,
  `lname` VARCHAR(255) NOT NULL,
  `phone` VARCHAR(255) NOT NULL,
  `no_exams_invigilated` INT UNSIGNED ZEROFILL NOT NULL,
  PRIMARY KEY (`staff_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `invigilators`.`class`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `invigilators`.`class` (
  `class_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `block_no` INT UNSIGNED NOT NULL,
  `capacity` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`class_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `invigilators`.`examhall`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `invigilators`.`examhall` (
  `class_id` INT UNSIGNED NOT NULL,
  INDEX `class_id_idx` (`class_id` ASC),
  CONSTRAINT `class_id`
    FOREIGN KEY (`class_id`)
    REFERENCES `invigilators`.`class` (`class_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `invigilators`.`subject`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `invigilators`.`subject` (
  `subject_id` INT UNSIGNED NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `programme` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`subject_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `invigilators`.`exam`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `invigilators`.`exam` (
  `subject_id` INT UNSIGNED NOT NULL,
  `semester` INT UNSIGNED NOT NULL,
  `programme` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`semester`, `programme`, `subject_id`),
  INDEX `subject_id_idx` (`subject_id` ASC),
  CONSTRAINT `subject_id`
    FOREIGN KEY (`subject_id`)
    REFERENCES `invigilators`.`subject` (`subject_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `invigilators`.`examinstance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `invigilators`.`examinstance` (
  `subject_id` INT UNSIGNED NOT NULL,
  `semester` INT UNSIGNED NOT NULL,
  `programme` VARCHAR(255) NOT NULL,
  `shift` INT UNSIGNED NOT NULL,
  `no_attendees` INT UNSIGNED NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`date`, `shift`),
  INDEX `subject_id_idx` (`subject_id` ASC),
  INDEX `semester_idx` (`semester` ASC),
  INDEX `programme_idx` (`programme` ASC),
  CONSTRAINT `subject_id`
    FOREIGN KEY (`subject_id`)
    REFERENCES `invigilators`.`exam` (`subject_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `semester`
    FOREIGN KEY (`semester`)
    REFERENCES `invigilators`.`exam` (`semester`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `programme`
    FOREIGN KEY (`programme`)
    REFERENCES `invigilators`.`exam` (`programme`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `invigilators`.`invigilator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `invigilators`.`invigilator` (
  `staff_id` INT UNSIGNED NOT NULL,
  `date` DATE NOT NULL,
  `class_id` INT UNSIGNED NOT NULL,
  INDEX `staff_id_idx` (`staff_id` ASC),
  INDEX `class_id_idx` (`class_id` ASC),
  INDEX `date_idx` (`date` ASC),
  CONSTRAINT `staff_id`
    FOREIGN KEY (`staff_id`)
    REFERENCES `invigilators`.`staff` (`staff_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `class_id`
    FOREIGN KEY (`class_id`)
    REFERENCES `invigilators`.`examhall` (`class_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `date`
    FOREIGN KEY (`date`)
    REFERENCES `invigilators`.`examinstance` (`date`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `invigilators`.`examin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `invigilators`.`examin` (
  `class_id` INT UNSIGNED NOT NULL,
  `subject_id` INT UNSIGNED NOT NULL,
  `semester` INT UNSIGNED NOT NULL,
  `programme` VARCHAR(255) NOT NULL,
  INDEX `class_id_idx` (`class_id` ASC),
  INDEX `subject_id_idx` (`subject_id` ASC),
  INDEX `semester_idx` (`semester` ASC),
  CONSTRAINT `class_id`
    FOREIGN KEY (`class_id`)
    REFERENCES `invigilators`.`examhall` (`class_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `subject_id`
    FOREIGN KEY (`subject_id`)
    REFERENCES `invigilators`.`exam` (`subject_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `semester`
    FOREIGN KEY (`semester`)
    REFERENCES `invigilators`.`exam` (`semester`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
