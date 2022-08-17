-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 17, 2022 at 08:22 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db`
--

-- --------------------------------------------------------

--
-- Table structure for table `record`
--

CREATE TABLE `record` (
  `id` int(11) NOT NULL,
  `stname` varchar(255) NOT NULL,
  `course` varchar(255) NOT NULL,
  `fee` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `record`
--

INSERT INTO `record` (`id`, `stname`, `course`, `fee`) VALUES
(1, '2', 'a', 0),
(125, 'pranto', 'cse', 12334),
(147, 'mou', 'cse', 7000),
(1122, 'fatima', 'eee', 6000),
(1132, 'jaba', 'cse', 5000),
(12345, 'nishat', 'cse', 50000),
(14445, 'niloy', 'cse', 1231245234);

-- --------------------------------------------------------

--
-- Table structure for table `registerdb`
--

CREATE TABLE `registerdb` (
  `id` int(11) NOT NULL,
  `user` varchar(30) NOT NULL,
  `pass` text NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `resis`
--

CREATE TABLE `resis` (
  `Examination` int(11) NOT NULL,
  `Year` text NOT NULL,
  `Semester` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `resiss`
--

CREATE TABLE `resiss` (
  `SL.NO` int(20) NOT NULL,
  `Course No` int(20) NOT NULL,
  `Course Title` int(20) NOT NULL,
  `Grade Point` int(20) NOT NULL,
  `Latter Grade` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `STUDID` varchar(200) NOT NULL,
  `FNAME` varchar(200) NOT NULL,
  `LNAME` varchar(200) NOT NULL,
  `ADDRESS` varchar(200) NOT NULL,
  `PHONE` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`STUDID`, `FNAME`, `LNAME`, `ADDRESS`, `PHONE`) VALUES
('20201125', '3', '2', 'B', '3'),
('20201147', '3', '2', 'A', '4'),
('20201149', '3', '1', 'B', '3'),
('asdasd', 'asdasd', 'asda', 'sdasd', 'asdasd');

-- --------------------------------------------------------

--
-- Table structure for table `student show`
--

CREATE TABLE `student show` (
  `uname` varchar(50) NOT NULL,
  `password` decimal(11,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `student show`
--

INSERT INTO `student show` (`uname`, `password`) VALUES
('pranto', '1125'),
('jaba', '1132'),
('prantokih', '1125');

-- --------------------------------------------------------

--
-- Table structure for table `students_db`
--

CREATE TABLE `students_db` (
  `STUDID` varchar(200) NOT NULL,
  `FNAME` varchar(200) NOT NULL,
  `LNAME` varchar(200) NOT NULL,
  `ADDRESS` varchar(200) NOT NULL,
  `PHONE` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `student_management_system`
--

CREATE TABLE `student_management_system` (
  `Roll_no` varchar(15) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Father_Name` varchar(55) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Category` varchar(10) NOT NULL,
  `Branch` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `Year` varchar(10) NOT NULL,
  `Contact_no` varchar(10) NOT NULL,
  `Address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `user` varchar(30) NOT NULL,
  `pass` text NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `user`, `pass`, `name`, `address`) VALUES
(1, 'nwu', '123456', 'pranto', 'pabla daulthpur'),
(2, 'jaba', '123456', 'pranto', 'kihpranto'),
(3, 'pranto', '123456', 'kih', 'ffererre');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `record`
--
ALTER TABLE `record`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registerdb`
--
ALTER TABLE `registerdb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `resis`
--
ALTER TABLE `resis`
  ADD PRIMARY KEY (`Examination`);

--
-- Indexes for table `resiss`
--
ALTER TABLE `resiss`
  ADD PRIMARY KEY (`SL.NO`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`STUDID`);

--
-- Indexes for table `students_db`
--
ALTER TABLE `students_db`
  ADD PRIMARY KEY (`STUDID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
