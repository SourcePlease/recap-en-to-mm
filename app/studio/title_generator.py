"""Burmese anime-recap title ideas: safe built-in templates plus optional AI suggestions."""
from __future__ import annotations

import re
from typing import Any

from studio.ai_providers import AIProviderError, chat_completion


TITLE_STYLES: dict[str, tuple[str, ...]] = {
    "Anime Recap": (
        "{title} — ဇာတ်လမ်းအကျဉ်း",
        "ဒီဇာတ်လမ်းရဲ့ အစကနေ အဆုံးထိ",
        "ဇာတ်လမ်းတစ်ခုလုံးကို အတိုချုံးကြည့်မယ်",
        "အစကနေ အဆုံးထိ မလွတ်တမ်း",
        "{title} ကို မိနစ်ပိုင်းအတွင်း ပြန်ကြည့်မယ်",
    ),
    "Isekai / Reincarnation": (
        "ပြန်လည်မွေးဖွားပြီး ကံကြမ္မာကို ပြောင်းလဲသူ",
        "နောက်ဘဝမှာ အင်အားကြီးဆုံး ဖြစ်လာသူ",
        "တခြားကမ္ဘာမှာ အသစ်စတင်ခဲ့တဲ့ ဘဝ",
        "{title} — ပြန်လည်မွေးဖွားခြင်းရဲ့ ဇာတ်လမ်း",
        "ဘဝသစ်မှာ အားလုံးကို အံ့ဩစေခဲ့သူ",
    ),
    "Overpowered / Action": (
        "တစ်ယောက်တည်းနဲ့ အားလုံးကို အနိုင်ယူသူ",
        "ဘယ်သူမှ မယှဉ်နိုင်တဲ့ အင်အား",
        "အားနည်းသူကနေ အင်အားအကြီးဆုံး ဖြစ်လာသူ",
        "{title} — စွမ်းအားအပြည့်နဲ့ တိုက်ပွဲများ",
        "တစ်ကြိမ်တည်းနဲ့ အားလုံးကို ပြောင်းလဲစေခဲ့သူ",
    ),
    "Dark Fantasy / Survival": (
        "အမှောင်ကမ္ဘာထဲက အသက်ရှင်ရေးတိုက်ပွဲ",
        "သေမင်းနဲ့ မျက်နှာချင်းဆိုင်ခဲ့ရတဲ့ နေ့ရက်များ",
        "မျှော်လင့်ချက်မရှိတဲ့ ကမ္ဘာထဲက ရှင်သန်မှု",
        "{title} — အမှောင်နောက်ကွယ်က လျှို့ဝှက်ချက်",
        "အသက်ရှင်ဖို့ အရာအားလုံးကို စွန့်စားရသူ",
    ),
    "Mystery / Twist": (
        "အဆုံးထိ မခန့်မှန်းနိုင်တဲ့ ဇာတ်လမ်း",
        "အားလုံးထင်ထားတာနဲ့ မတူတဲ့ အမှန်တရား",
        "နောက်ဆုံးအချိန်မှ ပေါ်လာတဲ့ လျှို့ဝှက်ချက်",
        "{title} — မထင်မှတ်ထားတဲ့ အလှည့်အပြောင်း",
        "တစ်ချက်မှားတာနဲ့ အရာအားလုံး ပြောင်းလဲသွားမယ်",
    ),
    "Romance / Betrayal": (
        "ချစ်ခြင်းရဲ့နောက်ကွယ်က သစ္စာဖောက်မှု",
        "တစ်ခါတည်းနဲ့ ပြောင်းလဲသွားတဲ့ ဆက်ဆံရေး",
        "အချစ်နဲ့ နာကျင်မှုကြားက ဇာတ်လမ်း",
        "{title} — မထင်မှတ်ထားတဲ့ အချစ်ဇာတ်လမ်း",
        "ယုံကြည်မှုတစ်ခု ပျက်စီးသွားတဲ့အခါ",
    ),
}


def _clean_source_title(value: str, max_chars: int = 100) -> str:
    value = str(value or "").replace("_", " ").replace(".", " ").strip()
    value = re.sub(r"\s+", " ", value)
    value = re.sub(r"(?i)\b(1080p|720p|480p|web[- ]?dl|bluray|x264|x265)\b", "", value)
    value = re.sub(r"\s+", " ", value).strip(" -_[]()")
    return value[:max_chars].strip()


def builtin_title_ideas(source_title: str, style: str = "Anime Recap") -> list[str]:
    """Return selectable titles without internet, credentials, or usage costs."""
    title = _clean_source_title(source_title) or "ဒီဇာတ်လမ်း"
    templates = TITLE_STYLES.get(style, TITLE_STYLES["Anime Recap"])
    result: list[str] = []
    for template in templates:
        idea = re.sub(r"\s+", " ", template.format(title=title)).strip()
        if idea and idea not in result:
            result.append(idea)
    return result


def ai_title_ideas(
    source_title: str,
    *,
    style: str = "Anime Recap",
    summary: str = "",
    provider: str,
    model: str,
    api_key: str | None = None,
    base_url: str | None = None,
    post=None,
    timeout: float = 35,
) -> list[str]:
    """Request up to six concise Burmese YouTube-title ideas from a configured text model."""
    title = _clean_source_title(source_title)
    if not title:
        raise AIProviderError("Enter a video/anime title first.")
    brief = _clean_source_title(summary, max_chars=700)
    prompt = f"""You are a Myanmar-language YouTube anime recap editor.
Return exactly six different thumbnail/headline title ideas in natural, fluent written Burmese.
Style category: {style}
Video/anime title: {title}
Optional plot notes (use only if supplied; do not invent specific plot facts): {brief or "(none supplied)"}
Rules:
- Keep each idea punchy, roughly 4–12 Burmese words, and readable on a thumbnail.
- Use curiosity, stakes, a transformation, mystery, or conflict where appropriate, but avoid fake facts.
- Mix title structures; don't repeat the anime name in every title.
- Do not add quotation marks, hashtags, explanations, English translations, or a numbered preamble.
- One title per line, in Burmese script where natural.
"""
    answer = chat_completion(
        provider, model, [{"role": "user", "content": prompt}],
        api_key=api_key, base_url=base_url, timeout=timeout, post=post,
    )
    ideas: list[str] = []
    for line in answer.splitlines():
        line = re.sub(r"^\s*(?:[-*•]|\d+[.)။]|[၀-၉]+[.)။])\s*", "", line).strip(" \t\"'“”‘’")
        line = re.sub(r"\s+", " ", line)
        if line and len(line) <= 150 and line not in ideas:
            ideas.append(line)
        if len(ideas) >= 6:
            break
    if not ideas:
        raise AIProviderError("The AI provider did not return any usable title ideas.")
    return ideas
