-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 19, 2019 at 12:31 PM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crop`
--

-- --------------------------------------------------------

--
-- Table structure for table `markets`
--

CREATE TABLE `markets` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `market_lat` float(20,8) DEFAULT NULL,
  `market_long` float(20,8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `markets`
--

INSERT INTO `markets` (`id`, `name`, `market_lat`, `market_long`) VALUES
(1, 'q', 18.52039909, 73.85669708);

-- --------------------------------------------------------

--
-- Table structure for table `market_crop_rel`
--

CREATE TABLE `market_crop_rel` (
  `id` int(11) NOT NULL,
  `market_id` int(11) DEFAULT NULL,
  `crop_name` varchar(100) DEFAULT NULL,
  `crop_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `market_crop_rel`
--

INSERT INTO `market_crop_rel` (`id`, `market_id`, `crop_name`, `crop_price`) VALUES
(0, 1, 'rie', 1000);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email_id` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `home_location_lat` float(20,8) DEFAULT NULL,
  `home_location_long` float(20,8) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email_id`, `password`, `home_location_lat`, `home_location_long`, `name`) VALUES
('h', 'h', 19.07283020, 72.88260651, 'h');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `markets`
--
ALTER TABLE `markets`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `market_crop_rel`
--
ALTER TABLE `market_crop_rel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `market_id` (`market_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `markets`
--
ALTER TABLE `markets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `market_crop_rel`
--
ALTER TABLE `market_crop_rel`
  ADD CONSTRAINT `market_crop_rel_ibfk_1` FOREIGN KEY (`market_id`) REFERENCES `markets` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
