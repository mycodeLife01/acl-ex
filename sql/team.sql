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

 Date: 14/03/2025 19:18:21
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for team
-- ----------------------------
DROP TABLE IF EXISTS `team`;
CREATE TABLE `team` (
  `team_id` int(11) NOT NULL AUTO_INCREMENT,
  `team_name` varchar(255) NOT NULL,
  `group` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `short_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of team
-- ----------------------------
BEGIN;
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (1, '从不招笑', 'A', 'tz');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (2, '大王叫我来巡山', 'B', 'Patrol');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (3, 'Reactivity king', 'C', 'Rtk');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (4, '嗨佬友特别定制无敌暴', 'D', 'TLG');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (5, '刚上b+轻虐', 'E', 'B+player');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (6, 'touchmyself', 'F', 'TMF');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (7, 'Twyz', 'G', 'Twyz');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (8, 'Phantom Force', 'H', 'PF');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (9, '300买条宽窄', 'I', 'UOB');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (10, '帆屿电竞 IDFJ', 'J', 'idfj');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (11, 'Awakened', 'K', 'AL');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (12, '风铃齐趣', 'L', 'FLQQ');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (13, '红孔雀歌舞厅.', NULL, 'PV');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (14, '五个小帅哥2.0', NULL, '5 HANDSOME');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (15, 'CTG', '', 'CTG');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (16, 'ZeroX', NULL, 'ZeroX');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (17, 'STAND OUT', NULL, 'STAND OUT');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (18, '五层汉堡', NULL, 'BURGERS');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (19, 'Magic cape', NULL, 'MAGIC CAPE');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (20, 'NBB', NULL, 'NBB');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (21, '成都SAG', NULL, 'SAG');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (22, 'ZhiWon', NULL, '指望');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (23, '1Tap.Gaming', NULL, '1Tap');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (24, 'Wenjiang whisky', NULL, 'WW');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (25, 'FIRE SIGNS', NULL, 'FS');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (26, '雪豹', NULL, 'SLP');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (27, '北洋CLAN', NULL, 'TJU');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (28, 'tycoon es', NULL, 'tycoon');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (29, '锦衣卫', NULL, '14 blades');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (30, '烬穹', NULL, 'Blaze Nova');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (31, 'Ture Or False', NULL, 'TOF');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (32, 'RavenGaurd', NULL, 'ADJ');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (33, '压力小子SK', NULL, 'SK-');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (34, '狂风', NULL, 'FW');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (35, '虾叽霸哒', NULL, 'BXDR');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (36, '吉林桥电竞', NULL, 'X1nQiao');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (37, '奶昔大王', NULL, 'NAIXI');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (38, 'Vahagn', NULL, 'Vahagn');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (39, 'wolf esport', NULL, 'WF');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (40, 'beer', NULL, 'beer');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (41, 'DK', NULL, 'DK');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (42, 'sawochup', NULL, 'SWC');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (43, 'XJ@u', NULL, 'XJau');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (44, '纯粹pro', NULL, 'chuncui');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (45, 'Reshape', NULL, 'Reshape');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (46, 'La licorne', NULL, 'La licorne');
INSERT INTO `team` (`team_id`, `team_name`, `group`, `short_name`) VALUES (47, '爱吃黑兰州', NULL, 'NW');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
