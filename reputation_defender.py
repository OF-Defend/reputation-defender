#!/usr/bin/env python3
"""
Reputation Defender
A reputation defense platform that helps individuals, creators, and businesses
monitor, identify, and respond to online reputation risks.

Analyzes a brand or name for negative search results, fake profiles, review
inconsistencies, missing business listings, and other digital trust signals,
then provides actionable recommendations to strengthen online visibility,
credibility, and brand protection.

https://www.of-defend.co
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def format_defense_type(defense_type: str) -> str:
    return " ".join(w.capitalize() for w in defense_type.split("-"))


def get_priority_action(scores: dict) -> str:
    labels = {
        "risk": "Risk",
        "trust_signal": "Trust Signal",
        "search_defense": "Search Defense",
        "profile_defense": "Profile Defense",
        "review_defense": "Review Defense",
        "listing_defense": "Listing Defense",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_defense_channels(search: int, profile: int, review: int, listing: int) -> dict:
    return {
        "Search Results": min(100, round(search * 1.0)),
        "Social Profiles": min(100, round(profile * 1.0)),
        "Review Platforms": min(100, round(review * 1.0)),
        "Business Listings": min(100, round(listing * 1.0)),
    }


def run_reputation_defender(
    brand: str,
    defense_type: str = "full-defense",
    risk_score: int = 88,
    trust_signal_score: int = 82,
    search_defense_score: int = 85,
    profile_defense_score: int = 78,
    review_defense_score: int = 90,
    listing_defense_score: int = 84,
) -> dict:
    """
    Run the Reputation Defender across all reputation defense signals.

    Args:
        brand: Brand name or individual identifier
        defense_type: Type of defense scan to run
        risk_score: Overall reputation risk score (0-100)
        trust_signal_score: Digital trust signal strength score (0-100)
        search_defense_score: Negative search defense score (0-100)
        profile_defense_score: Fake profile defense score (0-100)
        review_defense_score: Review defense and authenticity score (0-100)
        listing_defense_score: Business listing defense score (0-100)

    Returns:
        dict with individual defense scores, overall defense index,
        and defense channel breakdown
    """
    scores = {
        "risk": risk_score,
        "trust_signal": trust_signal_score,
        "search_defense": search_defense_score,
        "profile_defense": profile_defense_score,
        "review_defense": review_defense_score,
        "listing_defense": listing_defense_score,
    }
    overall_defense_index = round(sum(scores.values()) / 6)

    return {
        "brand": brand,
        "defense_type": format_defense_type(defense_type),
        "risk_score": risk_score,
        "trust_signal_score": trust_signal_score,
        "search_defense_score": search_defense_score,
        "profile_defense_score": profile_defense_score,
        "review_defense_score": review_defense_score,
        "listing_defense_score": listing_defense_score,
        "overall_defense_index": overall_defense_index,
        "priority_action": get_priority_action(scores),
        "defense_channels": get_defense_channels(search_defense_score, profile_defense_score, review_defense_score, listing_defense_score),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    brand = args[0] if len(args) > 0 else "brand-name"
    defense_type = args[1] if len(args) > 1 else "full-defense"
    risk_score = int(args[2]) if len(args) > 2 else 88
    trust_signal_score = int(args[3]) if len(args) > 3 else 82
    search_defense_score = int(args[4]) if len(args) > 4 else 85
    profile_defense_score = int(args[5]) if len(args) > 5 else 78
    review_defense_score = int(args[6]) if len(args) > 6 else 90
    listing_defense_score = int(args[7]) if len(args) > 7 else 84

    result = run_reputation_defender(
        brand, defense_type, risk_score, trust_signal_score,
        search_defense_score, profile_defense_score, review_defense_score, listing_defense_score
    )

    print(f"Brand: {result['brand']}")
    print(f"Defense Type: {result['defense_type']}")
    print("=" * 45)
    print(f"Risk Score:                    {result['risk_score']}/100  [{get_status(result['risk_score'])}]")
    print(f"Trust Signal Score:            {result['trust_signal_score']}/100  [{get_status(result['trust_signal_score'])}]")
    print(f"Search Defense Score:          {result['search_defense_score']}/100  [{get_status(result['search_defense_score'])}]")
    print(f"Profile Defense Score:         {result['profile_defense_score']}/100  [{get_status(result['profile_defense_score'])}]")
    print(f"Review Defense Score:          {result['review_defense_score']}/100  [{get_status(result['review_defense_score'])}]")
    print(f"Listing Defense Score:         {result['listing_defense_score']}/100  [{get_status(result['listing_defense_score'])}]")
    print("=" * 45)
    print(f"Overall Defense Index:         {result['overall_defense_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nDefense Channels:")
    for channel, score in result['defense_channels'].items():
        print(f"  {channel:<24} {score}/100")


if __name__ == "__main__":
    main()
