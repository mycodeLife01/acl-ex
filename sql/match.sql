/*
 Navicat Premium Dump SQL

 Source Server         : sh
 Source Server Type    : MySQL
 Source Server Version : 80018 (8.0.18)
 Source Host           : rm-uf6f326265lft8bwrdo.mysql.rds.aliyuncs.com:3306
 Source Schema         : acl_cs_2025

 Target Server Type    : MySQL
 Target Server Version : 80018 (8.0.18)
 File Encoding         : 65001

 Date: 14/03/2025 20:40:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for match
-- ----------------------------
DROP TABLE IF EXISTS `match`;
CREATE TABLE `match` (
  `match_id` varchar(255) NOT NULL,
  `schedual_id` varchar(255) NOT NULL,
  `match_start_time` int(11) NOT NULL,
  `match_end_time` int(11) NOT NULL,
  `winner` varchar(255) NOT NULL,
  `match_num` int(11) NOT NULL,
  PRIMARY KEY (`match_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

SET FOREIGN_KEY_CHECKS = 1;
