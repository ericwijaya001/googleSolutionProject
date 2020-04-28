-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2020 at 02:44 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `userdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `listbencana`
--

CREATE TABLE `listbencana` (
  `disasterTitle` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `id` int(11) NOT NULL,
  `disasterPhoto` varchar(50) NOT NULL,
  `donationMethod` varchar(50) NOT NULL,
  `disasterType` varchar(50) NOT NULL,
  `location` varchar(50) NOT NULL,
  `disasterDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='totalDonation';

--
-- Dumping data for table `listbencana`
--

INSERT INTO `listbencana` (`disasterTitle`, `description`, `id`, `disasterPhoto`, `donationMethod`, `disasterType`, `location`, `disasterDate`) VALUES
('bencanasatu', 'deskripsibencanasatu', 1, 'bencanasatu.jpg', 'transfer', 'jenismusibahsatu', 'lokasisatu', '1990-03-07'),
('bencanadua', 'deskripsibencanadua', 2, 'bencanadua.jpg', 'paypal', 'jenismusibahdua', 'lokasidua', '1991-02-23');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `isLogin` int(1) NOT NULL,
  `photo` text NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telp` int(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `total` int(50) NOT NULL,
  `anonymous` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `isLogin`, `photo`, `name`, `email`, `telp`, `address`, `total`, `anonymous`) VALUES
(1, 'orang1', 'b7298498ed622b562db707cb468a17eb', 1, 'mbo.jpg', 'namae_mbo', 'mbo@gmmail.com', 12345678, 'jalanalamat', 99999999, 0),
(2, 'mbo', 'asiapppppp', 1, 'mbo.jpg', 'mboname', 'emailmbo', 12345, 'jalanmbo', 0, 0),
(3, 'mbo1', 'asiapppppp', 1, 'mbo.jpg', 'mboname', 'emailmbo', 12345, 'jalanmbo', 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `listbencana`
--
ALTER TABLE `listbencana`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `listbencana`
--
ALTER TABLE `listbencana`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
