create database if not exists fabiaoqing;
use fabiaoqing;

# 创建类别表
create table if not exists category
(
    objectId   varchar(16)  not null comment '类别id,主键' primary key,
    name       varchar(255) not null comment '类别名称',
    `order`    int          not null comment '次序',
    createTime datetime     not null default CURRENT_TIMESTAMP comment '创建时间',
    updateTime datetime     not null default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP comment '更新时间'
);

# 创建分组表
create table if not exists `group`
(
    objectId   varchar(16) not null comment '分组id',
    name       varchar(255)         default '' not null comment '分组名称',
    parentId   varchar(16)          default '' not null comment '类别id（分组的父id）',
    `order`    int         not null comment '次序',
    createTime datetime    not null default CURRENT_TIMESTAMP comment '创建时间',
    updateTime datetime    not null default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP comment '更新时间',
    primary key (objectId, parentId) comment '复合主键，当分组id和类别id均不相同时，才认为不是一条记录'
);

# 创建表情表
create table if not exists emoticon
(
    objectId   varchar(16)  not null comment '表情包id',
    name       varchar(255)          default '' not null comment '表情包名称',
    url        varchar(255) not null comment '表情包地址',
    parentId   varchar(16)           default '' not null comment '表情包的分组id',
    `order`    int          not null comment '次序',
    createTime datetime     not null default CURRENT_TIMESTAMP comment '创建时间',
    updateTime datetime     not null default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP comment '更新时间',
    primary key (objectId, parentId) comment '复合主键，当表情包id和分组id均不相同时，才认为不是一条记录'
);