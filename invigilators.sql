-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 24, 2018 at 07:16 PM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `invigilators`
--

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `class_id` int(255) NOT NULL,
  `block_no` int(255) NOT NULL,
  `capacity` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `exam`
--

CREATE TABLE `exam` (
  `subject_id` int(255) NOT NULL,
  `semester` int(255) NOT NULL,
  `programme` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `examhall`
--

CREATE TABLE `examhall` (
  `class_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `examin`
--

CREATE TABLE `examin` (
  `semester` int(255) NOT NULL,
  `programme` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `subject_id` int(255) NOT NULL,
  `class_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `examinstance`
--

CREATE TABLE `examinstance` (
  `subject_id` int(255) NOT NULL,
  `semester` int(255) NOT NULL,
  `programme` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `shift` int(255) NOT NULL,
  `date` date NOT NULL,
  `no_attendees` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `invigilator`
--

CREATE TABLE `invigilator` (
  `staff_id` int(255) NOT NULL,
  `date` date DEFAULT NULL,
  `class_id` int(255) NOT NULL,
  `no_exams_invigilated` int(10) UNSIGNED ZEROFILL NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int(255) NOT NULL,
  `faculty` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `fname` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `lname` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `subject_id` int(255) NOT NULL,
  `title` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `programme` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`subject_id`, `title`, `programme`) VALUES
(1, 'database', 'bct'),
(2, 'artificial intelligence', 'bct');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`class_id`);

--
-- Indexes for table `exam`
--
ALTER TABLE `exam`
  ADD PRIMARY KEY (`subject_id`,`semester`,`programme`),
  ADD UNIQUE KEY `index_subject_id` (`subject_id`),
  ADD UNIQUE KEY `index_semester` (`semester`),
  ADD UNIQUE KEY `index_programme` (`programme`);

--
-- Indexes for table `examhall`
--
ALTER TABLE `examhall`
  ADD PRIMARY KEY (`class_id`);

--
-- Indexes for table `examin`
--
ALTER TABLE `examin`
  ADD PRIMARY KEY (`semester`,`programme`,`subject_id`,`class_id`),
  ADD KEY `index_class_id` (`class_id`) USING BTREE,
  ADD KEY `index_subject_id` (`subject_id`),
  ADD KEY `index_programme` (`programme`),
  ADD KEY `index_semester` (`semester`);

--
-- Indexes for table `examinstance`
--
ALTER TABLE `examinstance`
  ADD PRIMARY KEY (`subject_id`,`semester`,`programme`,`shift`,`date`),
  ADD KEY `index_subject_id` (`subject_id`) USING BTREE,
  ADD KEY `index_date` (`date`) USING BTREE,
  ADD KEY `index_shift` (`shift`) USING BTREE,
  ADD KEY `index_semester` (`semester`) USING BTREE,
  ADD KEY `index_programme` (`programme`) USING BTREE;

--
-- Indexes for table `invigilator`
--
ALTER TABLE `invigilator`
  ADD PRIMARY KEY (`staff_id`),
  ADD KEY `class_id` (`class_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_id`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`subject_id`,`programme`),
  ADD KEY `index_programme` (`programme`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `class_id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `subject`
--
ALTER TABLE `subject`
  MODIFY `subject_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `exam`
--
ALTER TABLE `exam`
  ADD CONSTRAINT `exam_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`);

--
-- Constraints for table `examhall`
--
ALTER TABLE `examhall`
  ADD CONSTRAINT `examhall_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`);

--
-- Constraints for table `examin`
--
ALTER TABLE `examin`
  ADD CONSTRAINT `examin_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `examhall` (`class_id`),
  ADD CONSTRAINT `examin_ibfk_2` FOREIGN KEY (`programme`) REFERENCES `exam` (`programme`),
  ADD CONSTRAINT `examin_ibfk_3` FOREIGN KEY (`semester`) REFERENCES `exam` (`semester`),
  ADD CONSTRAINT `examin_ibfk_4` FOREIGN KEY (`subject_id`) REFERENCES `exam` (`subject_id`);

--
-- Constraints for table `examinstance`
--
ALTER TABLE `examinstance`
  ADD CONSTRAINT `examinstance_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `exam` (`subject_id`),
  ADD CONSTRAINT `examinstance_ibfk_2` FOREIGN KEY (`semester`) REFERENCES `exam` (`semester`),
  ADD CONSTRAINT `examinstance_ibfk_3` FOREIGN KEY (`programme`) REFERENCES `exam` (`programme`);

--
-- Constraints for table `invigilator`
--
ALTER TABLE `invigilator`
  ADD CONSTRAINT `invigilator_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`staff_id`),
  ADD CONSTRAINT `invigilator_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `examhall` (`class_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
