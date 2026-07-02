#!/usr/bin/env python3
"""
AI Outreach Score Tool — $12
Quickly score and prioritize cold outreach leads by fit, intent, and engagement.
Usage: python3 ai_outreach_score.py leads.csv
"""

import csv
import json
import re
import sys
from datetime import datetime, date
from pathlib import Path


SCORING_RULES = {
    "industry_match": {"weight": 25, "description": "Prospect's industry matches your ICP"},
    "title_seniority": {"weight": 15, "description": "Decision-maker or influencer title (VP, Director, Head of, Founder, CEO, CTO, Owner)"},
    "company_size": {"weight": 10, "description": "Company size aligns with your target segment"},
    "trigger_event": {"weight": 20, "description": "Recent trigger event: funding, hiring spree, expansion, product launch, leadership change"},
    "channel_engagement": {"weight": 15, "description": "Prospect engaged with your content, follows your brand, or was referred"},
    "personalization": {"weight": 10, "description": "You have a specific hook or mutual connection"},
    "timeliness": {"weight": 5, "description": "Prospect likely in buying window this quarter"},
}


def score_industry_match(row):
    """Score how well the prospect's industry matches."""
    icp_industries = row.get("icp_industries", "").lower().split(",")
    prospect_industry = row.get("industry", "").lower().strip()
    if not prospect_industry:
        return 0
    for icp in icp_industries:
        if icp.strip() and (icp.strip() in prospect_industry or prospect_industry in icp.strip()):
            return 25
    return 5 if prospect_industry else 0


def score_title_seniority(row):
    """Score job title seniority."""
    title = row.get("title", "").lower().strip()
    senior_keywords = [
        "ceo", "cfo", "cto", "coo", "cmo", "chief", "vp", "vice president",
        "director", "head of", "founder", "owner", "partner", "president",
        "managing director", "principal",
    ]
    for keyword in senior_keywords:
        if keyword in title:
            return 15
    mid_keywords = ["manager", "lead", "senior", "lead", "team lead", "supervisor"]
    for keyword in mid_keywords:
        if keyword in title:
            return 8
    return 3 if title else 0


def score_company_size(row):
    """Score company size alignment."""
    try:
        employees = int(row.get("employees", 0))
    except (ValueError, TypeError):
        return 0

    target_min = int(row.get("target_min_employees", 0) or 0)
    target_max = int(row.get("target_max_employees", 999999) or 999999)

    if target_min <= employees <= target_max:
        return 10
    elif employees < target_min * 0.5:
        return 3
    elif employees > target_max * 2:
        return 2
    return 5


def score_trigger_event(row):
    """Score recent trigger events from the prospect's company."""
    triggers = row.get("trigger_events", "").lower().strip()
    if not triggers:
        return 0

    signal_keywords = [
        "funding", "raised", "series", "hiring", "expanding", "new office",
        "product launch", "partnership", "acquisition", "ipo", "rebrand",
        "leadership change", "new ceo", "new cto", "restructuring",
        "layoff", "rto", "return to office",
    ]
    score = 0
    for kw in signal_keywords:
        if kw in triggers:
            score += 5
    return min(score, 20)


def score_engagement(row):
    """Score prior engagement signals."""
    engagement = row.get("engagement_signals", "").lower().strip()
    score = 0
    signals = {
        "referred by": 15,
        "mutual connection": 10,
        "follows our brand": 8,
        "visited website": 5,
        "opened email": 3,
        "clicked link": 5,
        "attended webinar": 10,
        "downloaded content": 8,
        "connected on linkedin": 6,
        "engaged on social": 5,
    }
    for signal, points in signals.items():
        if signal in engagement:
            score += points
    return min(score, 15)


def score_personalization(row):
    """Score how personalized your approach can be."""
    hooks = row.get("personalization_hooks", "").strip()
    if not hooks:
        return 0
    hook_count = len([h for h in re.split(r'[.;,!]', hooks) if h.strip()])
    if hook_count >= 3:
        return 10
    elif hook_count >= 1:
        return 6
    return 2


def score_timeliness(row):
    """Score buying window proximity."""
    for field in ["buying_window", "timeline", "urgency"]:
        val = row.get(field, "").lower().strip()
        if "immediate" in val or "urgent" in val or "this quarter" in val:
            return 5
        if "next quarter" in val or "soon" in val:
            return 3
        if "exploring" in val or "researching" in val:
            return 2
    return 0


def calculate_total(row):
    return {
        "industry_match": score_industry_match(row),
        "title_seniority": score_title_seniority(row),
        "company_size": score_company_size(row),
        "trigger_event": score_trigger_event(row),
        "channel_engagement": score_engagement(row),
        "personalization": score_personalization(row),
        "timeliness": score_timeliness(row),
    }


def categorize(total_score, max_score=100):
    if total_score >= 80:
        return "🔥 HOT — reach out today"
    elif total_score >= 60:
        return "⚡ WARM — send personalized outreach"
    elif total_score >= 40:
        return "🌤️ LUKEWARM — add to nurture sequence"
    else:
        return "❄️ COLD — hold or remove from list"


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def generate_csv_output(leads, scores_list):
    output = "name,company,total_score,category,industry_match,title_seniority,company_size,trigger_event,engagement,personalization,timeliness\n"
    for lead, scores in zip(leads, scores_list):
        total = sum(scores.values())
        cat = categorize(total)
        output += (
            f"{lead.get('name','')},{lead.get('company','')},{total},{cat},"
            f"{scores['industry_match']},{scores['title_seniority']},{scores['company_size']},"
            f"{scores['trigger_event']},{scores['channel_engagement']},{scores['personalization']},{scores['timeliness']}\n"
        )
    return output


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ai_outreach_score.py leads.csv")
        print("\nThe CSV should have columns: name, company, title, industry, employees,")
        print("icp_industries, target_min_employees, target_max_employees, trigger_events,")
        print("engagement_signals, personalization_hooks, buying_window")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    leads = read_csv(path)
    if not leads:
        print("No leads found in CSV.")
        sys.exit(1)

    scores_list = [calculate_total(lead) for lead in leads]
    totals = [sum(s.values()) for s in scores_list]

    print("=" * 72)
    print(f"  AI OUTREACH SCORING REPORT — {date.today()}")
    print(f"  Leads scored: {len(leads)}")
    print("=" * 72)

    for i, (lead, scores, total) in enumerate(zip(leads, scores_list, totals), 1):
        print(f"\n  #{i} {lead.get('name', 'Unknown')} — {lead.get('company', 'Unknown')}")
        print(f"  {'─' * 60}")
        for dimension, score in scores.items():
            max_score = SCORING_RULES[dimension]["weight"]
            bar = "█" * int((score / max_score) * 10) if max_score > 0 else ""
            print(f"    {dimension.replace('_',' ').title():25s} {score:2d}/{max_score:2d} {bar}")
        print(f"  {'─' * 60}")
        print(f"  TOTAL: {total:2d}/100 — {categorize(total)}")
        print(f"  {'─' * 60}")

    # Summary
    hot = sum(1 for t in totals if t >= 80)
    warm = sum(1 for t in totals if 60 <= t < 80)
    lukewarm = sum(1 for t in totals if 40 <= t < 60)
    cold = sum(1 for t in totals if t < 40)

    print(f"\n  {'=' * 72}")
    print(f"  SUMMARY")
    print(f"  🔥 HOT:      {hot:3d} leads — prioritize immediate outreach")
    print(f"  ⚡ WARM:     {warm:3d} leads — send personalized this week")
    print(f"  🌤️ LUKEWARM: {lukewarm:3d} leads — add to nurture")
    print(f"  ❄️ COLD:     {cold:3d} leads — hold or archive")
    print(f"  {'=' * 72}")

    # Export scored CSV
    output_csv = f"scored_leads_{date.today()}.csv"
    with open(output_csv, "w") as f:
        f.write(generate_csv_output(leads, scores_list))
    print(f"\n  ✨ Exported: {output_csv}")
    print()


if __name__ == "__main__":
    main()
