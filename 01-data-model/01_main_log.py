#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import logging

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logger.logger_my import get_logger
from frenchdeck import FrenchDeck, Card
import random

# 配置日志
logger = get_logger(
    name='frenchdeck',
    log_file='../logs/frenchdeck.log',
    level=logging.DEBUG
)

def main():
    # 创建一个FrenchDeck实例
    deck = FrenchDeck()
    
    # 测试__len__方法
    logger.info("Deck length: {}".format(len(deck)))
    
    # 测试__getitem__方法 - 通过索引访问
    logger.info("First card: {}".format(deck[0]))
    logger.info("Last card: {}".format(deck[-1]))
    logger.info("Random card: {}".format(deck[10]))
    
    # 测试随机抽取牌
    logger.info("Random card (using random.choice): {}".format(random.choice(deck)))
    
    # 测试切片
    logger.info("First three cards:")
    for card in deck[:3]:
        logger.info("  {}".format(card))
    
    # 测试迭代
    logger.info("\nSome cards:")
    for card in deck[:5]:
        logger.info("  {}".format(card))
    
    # 测试in操作符
    logger.info("\nChecking if Card('Q', 'hearts') is in deck:")
    logger.info(Card('Q', 'hearts') in deck)
    logger.info("Checking if Card('7', 'beasts') is in deck:")
    logger.info(Card('7', 'beasts') in deck)


if __name__ == '__main__':
    main()
    logger.info("Test completed successfully")