-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 15, 2019 at 08:16 PM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.1.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `id` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` text NOT NULL,
  `id_proof` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `account_type` varchar(15) NOT NULL,
  `balance` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`id`, `name`, `address`, `id_proof`, `dob`, `account_type`, `balance`) VALUES
(1, 'kanthi', 'gajuwaka', '1234567890', '0000-00-00', 'savings', 10000),
(2, 'Bhaskar Satish', 'Murali Nagar', '276510986178', '0000-00-00', 'savings', 20000),
(3, 'Hari', 'Samatha nagar', '12344321', '0000-00-00', 'savings', 30000),
(4, 'Sudharshan', 'Vadlapudi', '12345432156', '1995-09-09', 'savings', 40000),
(5, 'Sharath', 'Kurmannapalem', '12345674543', '1995-06-21', 'savings', 50000),
(6, 'Pavan', 'bc road', '7874983724983824', '1995-12-08', 'savings', 60000),
(7, 'Bhargav', 'Gajuwaka', '3483748341', '1993-05-10', 'savings', 70000),
(8, 'Teja', 'car shed', '414324214314', '1992-01-01', 'savings', 80000),
(9, 'Nandan', 'Duvvada', '34124243432423', '1994-01-01', '/Library/Framew', 90000),
(10, 'Satish', 'muralinagar', '34324234', '1995-09-09', 'savings', 100000);

-- --------------------------------------------------------

--
-- Table structure for table `branch`
--

CREATE TABLE `branch` (
  `id` int(50) NOT NULL,
  `bank_name` varchar(50) NOT NULL,
  `branch` text NOT NULL,
  `code` int(5) NOT NULL,
  `ifsc` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `branch`
--

INSERT INTO `branch` (`id`, `bank_name`, `branch`, `code`, `ifsc`) VALUES
(1, 'SBI', 'Gajuwaka', 2716, 'SBIN0002716'),
(2, 'SBI', 'Kurmannapalem', 8998, 'SBIN0008998'),
(3, 'Lakshmi Vilas Bank', 'Gajuwaka', 279, 'LAVB0000279'),
(4, 'ICICI', 'Gajuwaka', 1108, 'ICIC0001108'),
(5, 'HDFC', 'Gajuwaka', 2813, 'HDFC0002813'),
(6, 'SBI', 'Dwarakanagar', 3060, 'SBIN0003060'),
(7, 'SBI', 'AKKAYYAPALEM', 5808, 'SBIN0015808');

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `id` int(50) NOT NULL,
  `date` datetime NOT NULL,
  `transaction_id` int(20) NOT NULL,
  `sender` varchar(50) NOT NULL,
  `receiver` varchar(50) NOT NULL,
  `mode` varchar(10) NOT NULL,
  `amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `branch`
--
ALTER TABLE `branch`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `branch`
--
ALTER TABLE `branch`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
