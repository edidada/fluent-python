#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os

def get_logger(name='app', log_file='../logs/app.log', level=logging.INFO):
    """
    获取配置好的logger实例
    
    Args:
        name: logger名称
        log_file: 日志文件路径
        level: 日志级别
    
    Returns:
        logging.Logger: 配置好的logger实例
    """
    # 确保日志目录存在
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 创建logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # 检查是否已有处理器，避免重复添加
    if not logger.handlers:
        # 创建文件处理器
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(level)
        
        # 设置日志格式
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        
        # 添加处理器到logger
        logger.addHandler(file_handler)
    
    return logger
