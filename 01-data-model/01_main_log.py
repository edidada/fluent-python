#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from frenchdeck import FrenchDeck, Card
import random

# 配置日志
logging.basicConfig(
    filename='../logs/frenchdeck.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def main():
    # 创建一个FrenchDeck实例
    deck = FrenchDeck()
    
    # 测试__len__方法
    logging.info("Deck length: {}".format(len(deck)))
    
    # 测试__getitem__方法 - 通过索引访问
    logging.info("First card: {}".format(deck[0]))
    logging.info("Last card: {}".format(deck[-1]))
    logging.info("Random card: {}".format(deck[10]))
    
    # 测试随机抽取牌
    logging.info("Random card (using random.choice): {}".format(random.choice(deck)))
    
    # 测试切片
    logging.info("First three cards:")
    for card in deck[:3]:
        logging.info("  {}".format(card))
    
    # 测试迭代
    logging.info("\nSome cards:")
    for card in deck[:5]:
        logging.info("  {}".format(card))
    
    # 测试in操作符
    logging.info("\nChecking if Card('Q', 'hearts') is in deck:")
    logging.info(Card('Q', 'hearts') in deck)
    logging.info("Checking if Card('7', 'beasts') is in deck:")
    logging.info(Card('7', 'beasts') in deck)


if __name__ == '__main__':
    main()
    logging.info("Test completed successfully")