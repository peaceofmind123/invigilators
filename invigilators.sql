-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 04, 2018 at 05:20 PM
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

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`class_id`, `block_no`, `capacity`) VALUES
(1, 23, 303),
(2, 234, 303);

-- --------------------------------------------------------

--
-- Table structure for table `exam`
--

CREATE TABLE `exam` (
  `subject_id` int(255) NOT NULL,
  `semester` int(255) NOT NULL,
  `programme` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `exam`
--

INSERT INTO `exam` (`subject_id`, `semester`, `programme`) VALUES
(3, 42, 'bct'),
(6, 5, 'bex');

-- --------------------------------------------------------

--
-- Table structure for table `examhall`
--

CREATE TABLE `examhall` (
  `class_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `examhall`
--

INSERT INTO `examhall` (`class_id`) VALUES
(1),
(2);

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

--
-- Dumping data for table `examin`
--

INSERT INTO `examin` (`semester`, `programme`, `subject_id`, `class_id`) VALUES
(42, 'bct', 3, 1);

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

--
-- Dumping data for table `examinstance`
--

INSERT INTO `examinstance` (`subject_id`, `semester`, `programme`, `shift`, `date`, `no_attendees`) VALUES
(3, 42, 'bct', 1, '2018-06-13', 30);

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

--
-- Dumping data for table `invigilator`
--

INSERT INTO `invigilator` (`staff_id`, `date`, `class_id`, `no_exams_invigilated`) VALUES
(1, '2018-06-05', 1, 0000000000),
(2, '2018-06-11', 2, 0000000000);

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

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `faculty`, `fname`, `lname`, `phone`) VALUES
(1, 'electronics and computer', 'aman', 'shakya', '9841414141'),
(2, 'science and humanities', 'sujan', 'lamichane', '9841212121');

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
(3, 'dbms1', 'bct'),
(4, 'ai', 'bct'),
(5, 'advanced electronics', 'bex'),
(6, 'DSAP', 'bex');

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
  ADD UNIQUE KEY `index_semester` (`semester`),
  ADD UNIQUE KEY `index_programme` (`programme`),
  ADD UNIQUE KEY `subject_id` (`subject_id`,`semester`,`programme`);

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
  ADD UNIQUE KEY `semester` (`semester`,`programme`,`subject_id`,`class_id`),
  ADD KEY `index_class_id` (`class_id`) USING BTREE,
  ADD KEY `index_subject_id` (`subject_id`),
  ADD KEY `index_programme` (`programme`);

--
-- Indexes for table `examinstance`
--
ALTER TABLE `examinstance`
  ADD PRIMARY KEY (`subject_id`,`semester`,`programme`,`shift`,`date`),
  ADD UNIQUE KEY `subject_id` (`subject_id`,`semester`,`programme`,`shift`,`date`),
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
  ADD KEY `invigilator_ibfk_2` (`class_id`);

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
  ADD UNIQUE KEY `subject_id` (`subject_id`,`programme`),
  ADD KEY `index_programme` (`programme`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `class_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `subject`
--
ALTER TABLE `subject`
  MODIFY `subject_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `exam`
--
ALTER TABLE `exam`
  ADD CONSTRAINT `exam_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `exam_ibfk_2` FOREIGN KEY (`programme`) REFERENCES `subject` (`programme`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `examhall`
--
ALTER TABLE `examhall`
  ADD CONSTRAINT `examhall_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `examin`
--
ALTER TABLE `examin`
  ADD CONSTRAINT `examin_ibfk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `examin_ibfk_2` FOREIGN KEY (`programme`) REFERENCES `subject` (`programme`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `examin_ibfk_3` FOREIGN KEY (`semester`) REFERENCES `exam` (`semester`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `examin_ibfk_4` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `examinstance`
--
ALTER TABLE `examinstance`
  ADD CONSTRAINT `examinstance_ibfk_1` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `examinstance_ibfk_2` FOREIGN KEY (`semester`) REFERENCES `exam` (`semester`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `examinstance_ibfk_3` FOREIGN KEY (`programme`) REFERENCES `subject` (`programme`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `invigilator`
--
ALTER TABLE `invigilator`
  ADD CONSTRAINT `invigilator_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`staff_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `invigilator_ibfk_2` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
