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

 Date: 14/03/2025 19:17:16
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for game_list
-- ----------------------------
DROP TABLE IF EXISTS `game_list`;
CREATE TABLE `game_list` (
  `match_code` varchar(255) NOT NULL COMMENT '每场比赛的唯一标识',
  `game_num` int(11) NOT NULL AUTO_INCREMENT COMMENT '本赛季第几场比赛',
  `match_week` int(11) NOT NULL COMMENT '比赛周',
  `match_day` int(11) NOT NULL COMMENT '比赛周中的比赛日',
  `match_num` int(11) NOT NULL COMMENT '比赛日的第几场比赛',
  `type` int(11) NOT NULL COMMENT '0代表bo1, 1代表bo3',
  `series` int(11) NOT NULL COMMENT '系列赛，每个bo1和bo3均代表一个系列赛',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间，默认当前时间',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间，默认当前时间，每次更新自动修改',
  `description` varchar(255) DEFAULT NULL COMMENT '第x周第x日第x场第x局',
  `Team1` varchar(255) NOT NULL,
  `Team2` varchar(255) NOT NULL,
  `win_team` varchar(255) NOT NULL,
  PRIMARY KEY (`match_code`),
  UNIQUE KEY `game_num` (`game_num`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='比赛列表';

-- ----------------------------
-- Records of game_list
-- ----------------------------
BEGIN;
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250215125720757972539', 6, 1, 1, 1, 0, 1, '2025-02-15 13:40:28', '2025-02-15 13:40:28', '', '从不招笑', '大王叫我来巡山', '大王叫我来巡山');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250215143139148072299', 7, 1, 1, 2, 0, 2, '2025-02-15 15:40:08', '2025-02-15 15:52:51', '', 'Reactivity king', '嗨佬友特别定制无敌暴', 'Reactivity king');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250215174335885102525', 8, 1, 1, 3, 0, 3, '2025-02-15 18:38:13', '2025-02-15 18:38:13', '', '刚上b+轻虐', 'touchmyself', '刚上b+轻虐');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250215200216395188813', 9, 1, 1, 4, 0, 4, '2025-02-15 21:00:42', '2025-02-15 21:00:42', '', 'Twyz', 'Phantom Force', 'Phantom Force');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250216124412631276472', 10, 1, 2, 1, 0, 5, '2025-02-16 13:54:29', '2025-02-16 13:54:29', '', '300买条宽窄', '帆屿电竞 IDFJ', '300买条宽窄');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250216151909933704295', 11, 1, 2, 2, 0, 6, '2025-02-16 16:01:16', '2025-02-16 16:01:16', '', 'Awakened', '风铃齐趣', 'Awakened');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250222130153491747569', 17, 2, 1, 1, 0, 7, '2025-02-22 14:03:01', '2025-02-22 14:03:01', '', '红孔雀歌舞厅.', '五个小帅哥2.0', '红孔雀歌舞厅.');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250222142139846188316', 18, 2, 1, 2, 0, 8, '2025-02-22 15:15:54', '2025-03-13 20:52:04', '', 'CTG', 'ZeroX', 'CTG');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250222162256767386714', 19, 2, 1, 3, 0, 9, '2025-02-22 17:06:48', '2025-02-22 17:06:48', '', 'CTG', 'STAND OUT', 'CTG');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250222174325463740010', 20, 2, 1, 4, 0, 10, '2025-02-22 18:51:02', '2025-03-13 20:51:51', '', '五层汉堡', '魔法披风Mc', '魔法披风Mc');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250222193348880707652', 22, 2, 1, 5, 0, 11, '2025-02-22 20:44:49', '2025-02-22 20:44:49', '', 'NBB Gaming', '成都SAG', '成都SAG');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250223123720131223881', 23, 2, 2, 1, 0, 12, '2025-02-23 13:41:46', '2025-02-23 13:41:46', '', '指望', '1Tap.Gaming', '指望');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250223145915317279212', 24, 2, 2, 2, 0, 13, '2025-02-23 15:34:02', '2025-02-23 15:34:02', '', '红孔雀歌舞厅.', 'WJ', '红孔雀歌舞厅.');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250223180427187776939', 25, 2, 2, 3, 0, 14, '2025-02-23 19:43:42', '2025-03-13 20:54:16', '', '1Tap.Gaming', 'Panthera', '1Tap');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250301125609996865527', 26, 3, 1, 1, 0, 15, '2025-03-01 14:25:57', '2025-03-01 14:25:57', '', '北洋CLAN', 'tycoon', 'tycoon');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250301143223064715702', 27, 3, 1, 2, 0, 16, '2025-03-01 15:29:51', '2025-03-01 15:29:51', '', '14 blades', 'BENA', '14 blades');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250301164920722050199', 28, 3, 1, 3, 1, 17, '2025-03-01 18:09:30', '2025-03-01 18:09:30', '', 'True Or False', 'RavenGaurd', 'TOF');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250301181240036691275', 29, 3, 1, 3, 1, 17, '2025-03-01 19:00:41', '2025-03-02 15:36:05', '', 'Ture Or False', 'RavenGaurd', 'TOF');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250302124122088784322', 30, 3, 2, 1, 0, 18, '2025-03-02 13:17:59', '2025-03-02 15:36:08', '', '压力小子sk', 'Fierce Wind.', 'FW');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250302143326583597226', 31, 3, 2, 2, 0, 19, '2025-03-02 15:26:47', '2025-03-02 15:36:11', '', '虾叽霸哒', '吉林桥电竞', 'BXDR');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250302162444221490003', 32, 3, 2, 3, 1, 20, '2025-03-02 17:33:55', '2025-03-02 17:33:55', '', '奶昔大王', 'Vahagn', 'Vahagn');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250302173503979701672', 33, 3, 2, 3, 1, 20, '2025-03-02 18:35:13', '2025-03-02 18:35:13', '', '奶昔大王', 'Vahagn', 'NAIXI');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250302183633410363154', 34, 3, 2, 3, 1, 20, '2025-03-02 19:27:34', '2025-03-02 19:27:34', '', '奶昔大王', 'Vahagn', 'Vahagn');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250308130230812949102', 35, 4, 1, 1, 1, 21, '2025-03-08 13:36:53', '2025-03-08 13:36:53', '', 'wolfesport', 'Beer', 'beer');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250308133635867593687', 36, 4, 1, 1, 1, 21, '2025-03-08 14:23:50', '2025-03-08 14:23:50', '', 'WF', 'BEER', 'beer');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250308160358706486775', 37, 4, 1, 2, 1, 22, '2025-03-08 16:49:46', '2025-03-08 16:49:46', '', 'MAGIC CAPE', 'AL', 'MAGIC CAPE');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250308165119749077489', 38, 4, 1, 2, 1, 22, '2025-03-08 17:34:16', '2025-03-08 20:13:18', '', 'MAGIC CAPE', 'AL', 'MAGIC CAPE');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250308184209760706516', 39, 4, 1, 3, 1, 23, '2025-03-08 19:28:22', '2025-03-08 20:13:21', '', 'DK', 'SWC', 'DK');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250308192813024074810', 40, 4, 1, 3, 1, 23, '2025-03-08 20:13:29', '2025-03-08 20:13:29', '', 'DK', 'SWC', 'DK');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250309124636476608016', 41, 4, 2, 1, 1, 24, '2025-03-09 13:34:33', '2025-03-09 13:34:33', '', 'ZHIWON', 'XJAU', 'XJau');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250309133447695101809', 42, 4, 2, 1, 1, 24, '2025-03-09 14:29:40', '2025-03-09 14:29:40', '', 'ZHIWON', 'XJAU', 'XJau');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250309155302463972030', 43, 4, 2, 2, 1, 25, '2025-03-09 17:11:37', '2025-03-09 17:11:37', '', 'CHUNCUI', 'RESHAPE', 'chuncui');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250309171534882008115', 44, 4, 2, 2, 1, 25, '2025-03-09 17:55:32', '2025-03-09 17:55:32', '', 'CHUNCUI', 'RESHAPE', 'chuncui');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250309185258838578377', 45, 4, 2, 3, 1, 26, '2025-03-09 19:41:08', '2025-03-09 19:41:08', '', 'NW', 'LA LICORNE', 'NW');
INSERT INTO `game_list` (`match_code`, `game_num`, `match_week`, `match_day`, `match_num`, `type`, `series`, `create_time`, `update_time`, `description`, `Team1`, `Team2`, `win_team`) VALUES ('g201-20250309193929389280492', 46, 4, 2, 3, 1, 26, '2025-03-09 20:29:11', '2025-03-09 20:29:11', '', 'NW', 'LA LICORNE', 'NW');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
