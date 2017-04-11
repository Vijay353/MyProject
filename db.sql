-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 16, 2016 at 04:40 AM
-- Server version: 10.1.16-MariaDB
-- PHP Version: 5.6.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Table structure for table `fee`
--

CREATE TABLE `fee` (
  `studentid` varchar(11) NOT NULL,
  `hostelid` varchar(30) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `roomno` int(3) NOT NULL,
  `hostelno` varchar(2) NOT NULL,
  `transactionid` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `h1`
--

CREATE TABLE `h1` (
  `studentid` varchar(11) NOT NULL,
  `hostelid` varchar(30) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `roomno` int(3) NOT NULL DEFAULT '0',
  `hostelno` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `h1`
--

INSERT INTO `h1` (`studentid`, `hostelid`, `studentname`, `roomno`, `hostelno`) VALUES
('2014ucp1234', '', 'shivom', 2, 'h1'),
('2014ucp1235', '', 'shivom', 3, 'h1'),
('2014ucp1236', '', 'shivom', 4, 'h1'),
('2014ucp1237', '', 'shivom', 5, 'h1'),
('2014ucp1238', '', 'shivom', 6, 'h1'),
('2014ucp1239', '', 'shivom', 7, 'h1'),
('2014ucp1240', '', 'shivom', 8, 'h1'),
('2014ucp1515', '', 'nikhil', 1, 'h1'),
('2014ucp8881', 'H114', 'VIJAY KUMAR', 14, 'h1'),
('2015ee1210', '', 'om', 12, 'h1'),
('2015ee1212', '', 'om', 9, 'h1'),
('2015ee1214', '', 'om', 10, 'h1'),
('2015ee1216', '', 'om', 13, 'h1'),
('2015ee1218', '', 'om', 11, 'h1');

-- --------------------------------------------------------

--
-- Table structure for table `h2`
--

CREATE TABLE `h2` (
  `studentid` varchar(11) NOT NULL,
  `hostelid` varchar(30) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `roomno` int(3) NOT NULL DEFAULT '0',
  `hostelno` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `h2`
--

INSERT INTO `h2` (`studentid`, `hostelid`, `studentname`, `roomno`, `hostelno`) VALUES
('2014uce1214', '', 'amit', 4, 'h2'),
('2014ucp1115', 'H26', 'VIJAY KUMAR', 6, 'h2'),
('2014ucp1511', 'H27', 'VIJAY KUMAR', 7, 'h2'),
('2014ucp1512', 'H28', 'VIJAY KUMAR', 8, 'h2'),
('2014ucp4444', 'H29', 'VIJAY KUMAR', 9, 'h2'),
('2014ucp4848', 'H25', 'omm', 5, 'h2'),
('2014ucp5555', 'H210', 'VIJAY KUMAR', 10, 'h2'),
('2014ucp6666', 'H211', 'VIJAY KUMAR', 11, 'h2'),
('2014ucp7777', 'H212', 'VIJAY KUMAR', 12, 'h2'),
('2014ucp8880', 'H216', 'VIJAY KUMAR', 16, 'h2'),
('2014ucp8888', 'H213', 'VIJAY KUMAR', 13, 'h2'),
('2014ucp9990', 'H215', 'VIJAY KUMAR', 15, 'h2'),
('2014ucp9999', 'H214', 'VIJAY KUMAR', 14, 'h2'),
('2014UEE1213', '', 'AMAN', 1, 'h2'),
('2015ee1212', '', 'om', 2, 'h2'),
('2015ee1216', '', 'om', 3, 'h2');

-- --------------------------------------------------------

--
-- Table structure for table `h3`
--

CREATE TABLE `h3` (
  `studentid` varchar(11) NOT NULL,
  `hostelid` varchar(30) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `roomno` int(3) NOT NULL DEFAULT '0',
  `hostelno` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `h3`
--

INSERT INTO `h3` (`studentid`, `hostelid`, `studentname`, `roomno`, `hostelno`) VALUES
('2014ucp1000', 'H39', 'VIJAY KUMAR', 9, 'h3'),
('2014ucp1102', '', 'himanshu', 5, 'h3'),
('2014ucp1112', 'H37', 'VIJAY KUMAR', 7, 'h3'),
('2014ucp1234', 'H38', 'VIJAY KUMAR', 8, 'h3'),
('2014ucp1393', '', 'himu', 6, 'h3'),
('2014ucp1513', '', 'annesh', 3, 'h3'),
('2014ucp1541', '', 'om', 1, 'h3'),
('2014ucp1544', '', 'om', 4, 'h3'),
('2014ucp1651', '', 'vijay', 2, 'h3');

-- --------------------------------------------------------

--
-- Table structure for table `h4`
--

CREATE TABLE `h4` (
  `studentid` varchar(11) NOT NULL,
  `hostelid` varchar(30) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `roomno` int(3) NOT NULL DEFAULT '0',
  `hostelno` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `h4`
--

INSERT INTO `h4` (`studentid`, `hostelid`, `studentname`, `roomno`, `hostelno`) VALUES
('2015ee1216', '', 'om', 1, 'h4'),
('2015ee1676', '', 'om', 2, 'h4');

-- --------------------------------------------------------

--
-- Table structure for table `h5`
--

CREATE TABLE `h5` (
  `studentid` varchar(11) NOT NULL,
  `hostelid` varchar(30) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `roomno` int(3) NOT NULL,
  `hostelno` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `h5`
--

INSERT INTO `h5` (`studentid`, `hostelid`, `studentname`, `roomno`, `hostelno`) VALUES
('2014ucp8889', 'H51', 'VIJAY KUMAR', 1, 'h5');

-- --------------------------------------------------------

--
-- Table structure for table `h6`
--

CREATE TABLE `h6` (
  `studentid` varchar(11) NOT NULL,
  `hostelid` varchar(30) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `roomno` int(3) NOT NULL,
  `hostelno` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `h7`
--

CREATE TABLE `h7` (
  `studentid` varchar(11) NOT NULL,
  `hostelid` varchar(30) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `roomno` int(3) NOT NULL,
  `hostelno` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `h8`
--

CREATE TABLE `h8` (
  `studentid` varchar(11) NOT NULL,
  `hostelid` varchar(30) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `roomno` int(3) NOT NULL,
  `hostelno` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `h8`
--

INSERT INTO `h8` (`studentid`, `hostelid`, `studentname`, `roomno`, `hostelno`) VALUES
('2014uch6666', 'h851', 'nisha', 51, 'h8');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `studentid` varchar(11) NOT NULL,
  `hostelid` varchar(30) NOT NULL,
  `studentname` varchar(30) NOT NULL,
  `fathername` varchar(30) NOT NULL,
  `dob` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `yoa` int(4) NOT NULL,
  `branch` varchar(30) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `email` varchar(30) NOT NULL,
  `contact` int(10) NOT NULL,
  `address` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `state` varchar(30) NOT NULL,
  `roomno` int(3) NOT NULL,
  `hostelno` varchar(2) NOT NULL,
  `transactionid` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`studentid`, `hostelid`, `studentname`, `fathername`, `dob`, `password`, `yoa`, `branch`, `gender`, `email`, `contact`, `address`, `city`, `state`, `roomno`, `hostelno`, `transactionid`) VALUES
('2014ucp1000', 'H39', 'VIJAY KUMAR', 'whg', '11/11/1996', '12', 2014, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'AUROBINDO HOSTEL , MNIT , JLN ', 'Jaipur', 'Rajasthan', 9, 'h3', ''),
('2014ucp1102', '', 'himanshu', 'om', '11/11/1995', '8888', 2014, 'computer', 'Male', 'abcd@gmail.com', 1233, 'sds', 'jjn', 'rajas', 5, 'h3', ''),
('2014ucp1112', 'H37', 'VIJAY KUMAR', 'ram', '11/11/1996', '1234', 2014, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 7, 'h3', ''),
('2014ucp1115', 'H26', 'VIJAY KUMAR', 'ram', '11/11/1996', '1234', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 6, 'h2', ''),
('2014ucp1234', 'H38', 'VIJAY KUMAR', 'rajam', '11/11/1996', '1', 2014, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'AUROBINDO HOSTEL , MNIT , JLN ', 'Jaipur', 'Rajasthan', 8, 'h3', ''),
('2014ucp1393', '', 'himu', 'himu', '11/11/1995', '123', 2014, 'electrical', 'Male', 'sas@gmail.com', 54545, 'ckdjcdj', 'jjn', 'raj', 6, 'h3', ''),
('2014ucp1511', 'H27', 'VIJAY KUMAR', 'ram', '11/11/1996', '1234', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 7, 'h2', ''),
('2014ucp1512', 'H28', 'VIJAY KUMAR', 'ram', '11/11/1996', '1234', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 8, 'h2', ''),
('2014ucp1541', '', 'om', 'om', '11/11/1995', '12', 2014, 'electrical', 'Male', 'daretosee@gmail.com', 48545454, 'AUROBINDO HOSTEL , MNIT , JLN ', 'Jaipur', 'Rajasthan', 1, 'h3', ''),
('2014ucp1544', '', 'om', 'om', '11/11/1995', '123', 2014, 'electrical', 'Male', 'ami.iamny@gmail.com', 48545454, 'efdrfr', 'jjn', 'rajas', 4, 'h3', ''),
('2014ucp4444', 'H29', 'VIJAY KUMAR', 'ram', '11/11/1996', '1234', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 9, 'h2', ''),
('2014ucp4848', 'H25', 'omm', 'omm', '11/11/1995', '12', 2015, 'electronics', 'Male', 'abcd@gmail.com', 6546565, 'deded', 'jaipur', 'rajasthan', 5, 'h2', ''),
('2014ucp5555', 'H210', 'VIJAY KUMAR', 'ram', '11/11/1996', '1234', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 10, 'h2', ''),
('2014ucp6666', 'H211', 'VIJAY KUMAR', 'ram', '11/11/1996', '12', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 11, 'h2', ''),
('2014ucp7777', 'H212', 'VIJAY KUMAR', 'ram', '11/11/1996', '34', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 12, 'h2', ''),
('2014ucp8880', 'H216', 'VIJAY KUMAR', 'ram', '11/11/1996', '12', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 16, 'h2', ''),
('2014ucp8881', 'H114', 'VIJAY KUMAR', 'ram', '11/11/1996', '12', 2016, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 14, 'h1', ''),
('2014ucp8888', 'H213', 'VIJAY KUMAR', 'ram', '11/11/1996', '56', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 13, 'h2', ''),
('2014ucp8889', 'H51', 'VIJAY KUMAR', 'ram', '11/11/1996', '45', 2016, 'computer', 'Female', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 1, 'h5', ''),
('2014ucp9990', 'H215', 'VIJAY KUMAR', 'ram', '11/11/1996', '12', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 15, 'h2', ''),
('2014ucp9999', 'H214', 'VIJAY KUMAR', 'ram', '11/11/1996', '56', 2015, 'computer', 'Male', 'daretosee@gmail.com', 2147483647, 'nhjvjs ', 'Jaipur', 'Rajasthan', 14, 'h2', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fee`
--
ALTER TABLE `fee`
  ADD PRIMARY KEY (`studentid`,`transactionid`);

--
-- Indexes for table `h1`
--
ALTER TABLE `h1`
  ADD PRIMARY KEY (`studentid`);

--
-- Indexes for table `h2`
--
ALTER TABLE `h2`
  ADD PRIMARY KEY (`studentid`);

--
-- Indexes for table `h3`
--
ALTER TABLE `h3`
  ADD PRIMARY KEY (`studentid`);

--
-- Indexes for table `h4`
--
ALTER TABLE `h4`
  ADD PRIMARY KEY (`studentid`);

--
-- Indexes for table `h6`
--
ALTER TABLE `h6`
  ADD PRIMARY KEY (`studentid`);

--
-- Indexes for table `h7`
--
ALTER TABLE `h7`
  ADD PRIMARY KEY (`studentid`);

--
-- Indexes for table `h8`
--
ALTER TABLE `h8`
  ADD PRIMARY KEY (`studentid`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`studentid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
