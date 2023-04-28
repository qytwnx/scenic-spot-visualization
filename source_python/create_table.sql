-- 创建库
CREATE DATABASE IF NOT EXISTS match_database;

-- 切换库
USE match_database;

# CREATE TABLE IF NOT EXISTS user
# (
#     id          INT AUTO_INCREMENT COMMENT 'id' PRIMARY KEY,
#     name        VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '姓名',
#     account     VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '手机号',
#     password    VARCHAR(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '密码',
#     role        VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '角色',
#     create_time DATETIME DEFAULT CURRENT_TIMESTAMP                            NOT NULL COMMENT '创建时间',
#     update_time DATETIME DEFAULT CURRENT_TIMESTAMP                            NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
#     CONSTRAINT uni_user_account
#         UNIQUE (account)
# ) COMMENT '用户' CHARSET = utf8mb4
#                  COLLATE = utf8mb4_unicode_ci;
# CREATE INDEX idx_user_name ON user (name);
# CREATE INDEX idx_user_account ON user (account);
#
# CREATE TABLE IF NOT EXISTS files
# (
#     id          INT AUTO_INCREMENT COMMENT 'id' PRIMARY KEY,
#     name        VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci  NOT NULL COMMENT '文件名',
#     type        VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci  NOT NULL COMMENT '类型',
#     size        VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci  NOT NULL COMMENT '文件大小',
#     url         VARCHAR(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL COMMENT '下载链接',
#     uploader    int                                                            NOT NULL COMMENT '上传者',
#     create_time DATETIME DEFAULT CURRENT_TIMESTAMP                             NOT NULL COMMENT '创建时间',
#     update_time DATETIME DEFAULT CURRENT_TIMESTAMP                             NOT NULL on update CURRENT_TIMESTAMP COMMENT '更新时间'
# ) COMMENT '文件' CHARSET = utf8mb4
#                  COLLATE = utf8mb4_unicode_ci;
# CREATE INDEX idx_file_name ON files (name);
# CREATE INDEX idx_file_type ON files (type);
#
# CREATE TABLE IF NOT EXISTS operation_log
# (
#     id             INT AUTO_INCREMENT COMMENT 'id' PRIMARY KEY,
#     method         VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '请求方式',
#     url            VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '请求URL',
#     ip             VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '主机地址',
#     param          TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci COMMENT '请求参数',
#     operation_time DATETIME                                                      DEFAULT CURRENT_TIMESTAMP NOT NULL COMMENT '操作'
# ) COMMENT '操作日志记录' CHARSET = utf8mb4
#                          COLLATE = utf8mb4_unicode_ci;
# CREATE INDEX idx_operation_method ON operation_log (method);
# CREATE INDEX idx_operation_time ON operation_log (operation_time);


CREATE TABLE IF NOT EXISTS scenic_spots
(
    id           INT AUTO_INCREMENT COMMENT 'id' PRIMARY KEY,
    name         VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci  DEFAULT '' COMMENT '景区名字',
    level        VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci  DEFAULT '' COMMENT '景区等级',
    province     VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci  DEFAULT '' COMMENT '省',
    city         VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci  DEFAULT '' COMMENT '市',
    address      VARCHAR(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '地址',
    introduction TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci COMMENT '简介',
    heat         VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci  DEFAULT '' COMMENT '热度',
    price        VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci  DEFAULT '' COMMENT '价格',
    sales        VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci  DEFAULT '' COMMENT '月销',
    image        VARCHAR(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '图片',
    info         VARCHAR(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '资讯',
    comment      VARCHAR(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT '评论',
    create_time  DATETIME                                                       DEFAULT CURRENT_TIMESTAMP NOT NULL COMMENT '创建时间',
    update_time  DATETIME                                                       DEFAULT CURRENT_TIMESTAMP NOT NULL on update CURRENT_TIMESTAMP COMMENT '更新时间'
) COMMENT '景点' CHARSET = utf8mb4
                 COLLATE = utf8mb4_unicode_ci;
CREATE INDEX idx_scenic_spots_name ON scenic_spots (name);