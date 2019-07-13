create database if not exists fabiaoqing;
use fabiaoqing;

# 创建类别表
CREATE TABLE if not exists `t_category`
(
    `object_id`   varchar(16)  NOT NULL COMMENT '类别id',
    `name`        varchar(255) NOT NULL COMMENT '类别名称',
    `seq`         int(11)      NOT NULL COMMENT '次序',
    `create_time` datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`object_id`) USING BTREE COMMENT '主键'
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

# 创建表情包表
CREATE TABLE if not exists `t_package`
(
    `object_id`   varchar(16)  NOT NULL COMMENT '分组id',
    `name`        varchar(255) NOT NULL DEFAULT '' COMMENT '分组名称',
    `parent_id`   varchar(16)  NOT NULL DEFAULT '' COMMENT '类别id（分组的父id）',
    `seq`         int(11)      NOT NULL COMMENT '次序',
    `create_time` datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`object_id`, `parent_id`) USING BTREE COMMENT '复合主键，当分组id和类别id均不相同时，才认为不是一条记录'
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

# 创建表情表
CREATE TABLE if not exists `t_emoticon`
(
    `object_id`   varchar(16)  NOT NULL COMMENT '表情包id',
    `name`        varchar(255) NOT NULL DEFAULT '' COMMENT '表情包名称',
    `url`         varchar(255) NOT NULL COMMENT '表情包地址',
    `parent_id`   varchar(16)  NOT NULL DEFAULT '' COMMENT '表情包的分组id',
    `seq`         int(11)      NOT NULL COMMENT '次序',
    `create_time` datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`object_id`, `parent_id`) USING BTREE COMMENT '复合主键，当表情包id和分组id均不相同时，才认为不是一条记录'
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE if not exists `t_tag`
(
    `object_id`   varchar(16)  NOT NULL COMMENT '标签id',
    `name`        varchar(255) NOT NULL DEFAULT '' COMMENT '标签名称',
    `create_time` datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` datetime     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`object_id`) USING BTREE COMMENT '主键'
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;