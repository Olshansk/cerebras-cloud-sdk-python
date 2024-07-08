# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from cerebras_cloud_sdk import Cerebras, AsyncCerebras
from cerebras_cloud_sdk.types.chat import ChatCompletion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cerebras) -> None:
        completion = client.chat.completions.create(
            messages=[{"role": "user"}],
            model="llama3-8b-8192",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cerebras) -> None:
        completion = client.chat.completions.create(
            messages=[
                {
                    "content": "What is 1+1?",
                    "role": "user",
                }
            ],
            model="llama3-8b-8192",
            max_tokens=0,
            prompt="string",
            seed=0,
            stop_sequence="string",
            stream=True,
            temperature=0,
            top_p=0,
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cerebras) -> None:
        response = client.chat.completions.with_raw_response.create(
            messages=[{"role": "user"}],
            model="llama3-8b-8192",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cerebras) -> None:
        with client.chat.completions.with_streaming_response.create(
            messages=[{"role": "user"}],
            model="llama3-8b-8192",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(ChatCompletion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCerebras) -> None:
        completion = await async_client.chat.completions.create(
            messages=[{"role": "user"}],
            model="llama3-8b-8192",
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCerebras) -> None:
        completion = await async_client.chat.completions.create(
            messages=[
                {
                    "content": "What is 1+1?",
                    "role": "user",
                }
            ],
            model="llama3-8b-8192",
            max_tokens=0,
            prompt="string",
            seed=0,
            stop_sequence="string",
            stream=True,
            temperature=0,
            top_p=0,
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCerebras) -> None:
        response = await async_client.chat.completions.with_raw_response.create(
            messages=[{"role": "user"}],
            model="llama3-8b-8192",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCerebras) -> None:
        async with async_client.chat.completions.with_streaming_response.create(
            messages=[{"role": "user"}],
            model="llama3-8b-8192",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(ChatCompletion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True