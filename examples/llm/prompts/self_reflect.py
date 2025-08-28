#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Time:
    2025-08-28 18:54:06
Author:
    huayang (imhuay@163.com)
Subject:
    self_reflect
References:
    None
"""

from __future__ import annotations

import os
from typing import Any, Callable, Dict, List

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def create(messages: list, model: str = 'gpt-4o-mini', **kw):
    """"""
    response = client.chat.completions.create(model=model, messages=messages, temperature=0.3, **kw)
    return response.choices[0].message.content


class SelfReflector:
    """
    自反思 Agent：
    1. Thought
    2. Critique
    3. Revision
    循环直到 critique 说“无需改进”或达到 max_rounds
    """

    _default_system_prompt = 'You are a helpful assistant.'
    _default_critique_prompt = (
        '请对上面刚给出的答案进行批判性审查。检查逻辑漏洞、事实错误、表达不清等问题，并给出具体、可操作的改进建议。'
        '如果答案已无可挑剔，请直接回复“无需改进”。'
    )
    _default_revise_prompt = (
        '根据上面的批判意见，请给出改进后的完整答案。务必保留并强化原答案的优点，同时修正被指出的问题。'
    )

    def __init__(
        self,
        system_prompt: str | Callable[[], str] | None = None,
        critique_prompt: str | Callable[[str], str] | None = None,
        revise_prompt: str | Callable[[str, str], str] | None = None,
        max_rounds: int = 2,
        create_fn: Callable[..., str] = create,
    ):
        self.system_prompt = system_prompt or self._default_system_prompt
        self.critique_prompt = critique_prompt or self._default_critique_prompt
        self.revise_prompt = revise_prompt or self._default_revise_prompt

        self.max_rounds = max_rounds
        self.create = create_fn

    def run(self, question: str) -> str:
        """
        基于 Copilot 的示例: https://copilot.microsoft.com/shares/T4p7zRcEWj83TmKKb5kng
        """
        messages = [
            {'role': 'system', 'content': self.system_prompt},
            {'role': 'user', 'content': question},
        ]

        for rnd in range(1, self.max_rounds + 1):
            # 1. Thought / Revision
            print(f'=== Round {rnd} ===')
            answer = self.create(messages)
            messages.append({'role': 'assistant', 'content': answer})
            print(f'--- Thought ---\n{answer}\n')

            # 2. Critique
            messages.append({'role': 'user', 'content': self.critique_prompt})
            critique = self.create(messages)
            messages.append({'role': 'assistant', 'content': critique})
            print(f'--- Critique ---\n{critique}\n')

            if '无需改进' in critique or rnd == self.max_rounds:
                break

            # 3. Revise
            messages.append({'role': 'user', 'content': self.revise_prompt})

        return answer
