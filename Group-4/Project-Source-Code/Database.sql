-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 05, 2022 at 10:26 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vms`
--

-- --------------------------------------------------------

--
-- Table structure for table `case_info`
--

CREATE TABLE `case_info` (
  `c_id` int(11) NOT NULL,
  `c_det` varchar(255) DEFAULT NULL,
  `reg` varchar(255) DEFAULT NULL,
  `ser_id` varchar(255) DEFAULT NULL,
  `taka` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `case_info`
--

INSERT INTO `case_info` (`c_id`, `c_det`, `reg`, `ser_id`, `taka`) VALUES
(112233452, 'dfgdfgsdfgsv', '123456', '1234', '45525'),
(112233453, 'dfgsgdfssdfg', '123456', '1234', '23412'),
(112233454, 'efwefw', '128639', '1234', '12343'),
(112233455, 'frfraegr', '1234567', '1342234', '345354'),
(112233456, 'dfghxhg', '125170', '123', '2000');

-- --------------------------------------------------------

--
-- Table structure for table `log_in`
--

CREATE TABLE `log_in` (
  `id` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `log_in`
--

INSERT INTO `log_in` (`id`, `pass`) VALUES
('20201136010', 'nwu'),
('20201153010', 'nwu'),
('20201122010', 'nwu'),
('habib', '20201136010'),
('fatima', '20201122010'),
('jyoti', '20201153010');

-- --------------------------------------------------------

--
-- Table structure for table `own_log`
--

CREATE TABLE `own_log` (
  `id` varchar(40) NOT NULL,
  `pass` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `own_log`
--

INSERT INTO `own_log` (`id`, `pass`) VALUES
('habib', '128639'),
('fatima', '125170'),
('habib', '121314'),
('habib', '123456'),
('fgd', 'dsfg'),
('gxbd', 'xdg'),
('fng', 'dhst'),
('fng', 'dhst'),
('fng', 'dhst'),
('dnfgx', 'dnfg'),
('bdfg', '4563'),
('bdfg2', '4563456'),
('bdfg23', '45634563'),
('bdfg234', '456345634'),
('bdfg2345', '4563456345'),
('bdfg23456', '45634563456'),
('bdfg234567', '456345634567'),
('bdfg2345678', '4563456345678'),
('bdfg2345678', '4563456345678'),
('habib', '128639'),
('123', '123');

-- --------------------------------------------------------

--
-- Table structure for table `rep`
--

CREATE TABLE `rep` (
  `reg` varchar(40) NOT NULL,
  `claim_det` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `rep`
--

INSERT INTO `rep` (`reg`, `claim_det`) VALUES
('123456', 'wrong owner name'),
('125170', 'gjyjrtdhtrgh');

-- --------------------------------------------------------

--
-- Table structure for table `ser_log_in`
--

CREATE TABLE `ser_log_in` (
  `id` varchar(40) NOT NULL,
  `pass` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ser_log_in`
--

INSERT INTO `ser_log_in` (`id`, `pass`) VALUES
('365432', '1234'),
('156480', '1234'),
('123', '123');

-- --------------------------------------------------------

--
-- Table structure for table `vms_info`
--

CREATE TABLE `vms_info` (
  `type` varchar(40) NOT NULL,
  `c_name` varchar(40) NOT NULL,
  `model` varchar(40) NOT NULL,
  `origin` varchar(40) NOT NULL,
  `capasity` varchar(40) NOT NULL,
  `color` varchar(40) NOT NULL,
  `name` varchar(40) NOT NULL,
  `reg` varchar(40) NOT NULL,
  `m_date` varchar(40) NOT NULL,
  `e_num` varchar(40) NOT NULL,
  `c_num` varchar(40) NOT NULL,
  `weight` varchar(40) NOT NULL,
  `r_date` varchar(40) NOT NULL,
  `b_from` varchar(40) NOT NULL,
  `price` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vms_info`
--

INSERT INTO `vms_info` (`type`, `c_name`, `model`, `origin`, `capasity`, `color`, `name`, `reg`, `m_date`, `e_num`, `c_num`, `weight`, `r_date`, `b_from`, `price`) VALUES
('car', 'honda', 'x-trail', 'japan', '5', 'black', 'dfyh', '64576', '12/12/12', '46565436', '865235563', '776', '12/12/12', 'khulna', '5363653'),
('bdfg', 'dfb', 'bdf', 'bdfx', '45', 'bdfx', 'bdfg', '4563', '7/28/22', '67567', '72453', '456', '7/28/22', 'dfg', '456678'),
('bdfg2', 'dfb2', 'bdf2', 'bdfx2', '452', 'bdfx2', 'bdfg2', '4563456', '7/28/22', '675672', '724532', '4562', '7/28/22', 'dfg2', '4566782'),
('bdfg23', 'dfb23', 'bdf23', 'bdfx23', '4523', 'bdfx23', 'bdfg23', '45634563', '7/28/22', '6756723', '7245323', '45623', '7/28/22', 'dfg23', '45667823'),
('bdfg234', 'dfb234', 'bdf234', 'bdfx234', '45234', 'bdfx234', 'bdfg234', '456345634', '7/28/22', '67567234', '72453234', '456234', '7/28/22', 'dfg234', '456678234'),
('bdfg2345', 'dfb2345', 'bdf2345', 'bdfx2345', '452345', 'bdfx2345', 'habib', '4563456345', '7/28/22', '675672345', '724532345', '4562345', '7/28/22', 'dfg2345', '4566782345'),
('bdfg23456', 'dfb23456', 'bdf23456', 'bdfx23456', '4523456', 'bdfx23456', 'bdfg23456', '45634563456', '7/28/22', '6756723456', '7245323456', '45623456', '7/28/22', 'dfg23456', '45667823456'),
('bdfg234567', 'dfb234567', 'bdf234567', 'bdfx234567', '45234567', 'bdfx234567', 'bdfg234567', '456345634567', '7/28/22', '67567234567', '72453234567', '456234567', '7/28/22', 'dfg234567', '456678234567');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `case_info`
--
ALTER TABLE `case_info`
  ADD PRIMARY KEY (`c_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `case_info`
--
ALTER TABLE `case_info`
  MODIFY `c_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=112233457;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
