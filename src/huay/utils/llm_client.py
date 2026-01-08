#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2026-01-08 21:37:32
Author:
    huayang (imhuay@163.com)
Subject:
    llm_client
References:
    None
"""

from __future__ import annotations

import os

import openai
from openai import OpenAI


class LLMClient:
    """"""

    def __init__(self) -> None:
        pass

    def _build_client(self):
        """"""

    @staticmethod
    def demo_by_bailian():
        # DASHSCOPE_API_KEY = 'sk-***'

        client = OpenAI(
            # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
            base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
            # api_key=DASHSCOPE_API_KEY,
            api_key=os.getenv('DASHSCOPE_API_KEY'),
        )

        completion = client.chat.completions.create(
            # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
            model="qwen-plus",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "你是谁？"},
            ]
        )
        # print(completion.model_dump_json())
        print(completion.choices[0].message)
        
    
    @staticmethod
    def demo_by_huggingface():
        """"""
        # HF_TOKEN = 'hf_***'
        
        client = OpenAI(
            base_url='https://router.huggingface.co/v1',
            # api_key=HF_TOKEN,
            api_key=os.environ['HF_TOKEN'],
        )

        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": "What is the capital of France?"
                }
            ],
        )

        print(completion.choices[0].message)
        
    

if __name__ == '__main__':
    """"""
    client = LLMClient()

    client.demo_by_bailian()