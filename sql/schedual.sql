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

 Date: 14/03/2025 19:18:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for schedual
-- ----------------------------
DROP TABLE IF EXISTS `schedual`;
CREATE TABLE `schedual` (
  `schedual_id` varchar(255) NOT NULL,
  `season_id` int(11) NOT NULL,
  `schedual_name` varchar(255) NOT NULL,
  `schedual_start_time` bigint(20) NOT NULL,
  `schedual_status` varchar(255) NOT NULL,
  `team_1` varchar(255) NOT NULL,
  `team_2` varchar(255) NOT NULL,
  `team_1_score` int(11) NOT NULL,
  `team_2_score` int(11) NOT NULL,
  `stage_id` int(11) NOT NULL,
  `stage_name` varchar(255) NOT NULL,
  PRIMARY KEY (`schedual_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of schedual
-- ----------------------------
BEGIN;
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
