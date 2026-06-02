# Reasoning Log: Will any Nvidia N1- or N1X-powered Windows PC be available for purchase by consumers before June 14, 2026?

*Generated: 2026-06-02T01:39:50.449685+00:00*


## 💭 Thinking

Let me analyze this forecasting question about whether any Nvidia N1- or N1X-powered Windows PC will be available for purchase by consumers before June 14, 2026.

Key elements:
- The question asks about consumer availability between May 31, 2026 and June 13, 2026 (23:59 UTC)
- Computex 2026 keynote is May 31-June 1, Microsoft Build follows June 2
- The question was published June 2, 2026 and closes June 2, 2026
- Resolution is June 13, 2026

Let me research the current state of Nvidia N1/N1X announcements and any availability information.

## 💬 Response

I'll start by parsing the resolution criteria and researching the current state of Nvidia N1/N1X announcements.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    43745
  ]
}
```

### 📋 Result

```
{"post_id": 43745, "title": "Will any Nvidia N1- or N1X-powered Windows PC be available for purchase by consumers before June 14, 2026?", "type": "binary", "url":
"https://www.metaculus.com/questions/43745", "background_info": "In late May 2026, Nvidia and Microsoft posted coordinated \"a new era of PC\" teasers pointing to Jensen Huang's Computex 2026 keynote
in Taipei (May 31\u2013June 1, 2026), with Microsoft's Build conference following on June 2. Industry coverage (Tom's Hardware, Windows Central, TechSpot, TweakTown) widely interprets the teaser as
the formal debut of Nvidia's long-rumored ARM-based \"N1\" and \"N1X\" SoCs \u2014 co-designed with MediaTek and featuring a ~20-core ARM CPU paired with an RTX-class integrated GPU \u2014 running
Windows on Arm.\n\nThe N1/N1X program was originally targeted for a Q3 2025 launch but was reportedly delayed into 2026 due to Windows on Arm software readiness, silicon revisions, and memory
supply/notebook-demand headwinds. Leaks reference Dell, Lenovo, and possibly Alienware systems \"being prepared for 2026,\" and a leaked motherboard image surfaced for an N1 laptop reportedly
retailing around $1,400. However, no OEM has publicly committed to an on-sale date, and the typical gap between a Computex unveil and retail availability of a brand-new silicon platform is measured in
months, not weeks.\n\nThis question asks whether any consumer can actually buy an N1- or N1X-powered Windows PC in the roughly two weeks between the expected Computex/Build announcements and June 14,
2026.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 4, \"ambiguity\": 4, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question resolves YES if,
at any point between May 31, 2026 and 23:59 UTC on June 13, 2026, a Windows-based personal computer (laptop, desktop, mini-PC, or 2-in-1) whose primary system-on-chip is marketed by Nvidia and/or its
OEM partners as the Nvidia \"N1\" or \"N1X\" (or a variant clearly using the same SoC family, e.g., \"N1X Max\") is offered for sale to ordinary consumers in at least one country, with the ability to
place an order and receive shipment (or in-store pickup) of the device. Evidence can include a working \"Buy\" or \"Add to Cart\" button with stated availability/ship date on the website of a major
OEM (e.g., Dell, Lenovo, HP, Asus, Acer, MSI, Microsoft, Alienware, Razer, Samsung) or a major retailer (e.g., Best Buy, Amazon, Newegg, JD.com), or a reputable news report from [credible
sources](https://www.metaculus.com/faq/#definitions) confirming that such a device has gone on sale to consumers.\n\nPre-orders count as \"available for purchase\" ONLY if the OEM/retailer accepts
payment or a binding order with a stated estimated ship date on or before July 31, 2026. Pure \"register your interest,\" \"notify me,\" or \"coming soon\" listings do NOT count. Developer kits,
engineering samples, enterprise-only/B2B-only SKUs not offered to individual consumers, and the existing Nvidia DGX Spark / GB10-based mini-PC (which is a separate product line, not branded N1/N1X)
also do NOT count.\n\nIf no such consumer-purchasable N1/N1X Windows PC is documented by 23:59 UTC on June 13, 2026, the question resolves NO.", "fine_print": "If Nvidia and partners brand the chip
with a different final retail name at launch (e.g., the SoC long rumored as \"N1X\" ships under a different marketing name), a device using that chip still counts as long as reputable reporting or
Nvidia's own materials identify it as the same silicon previously referred to as N1 or N1X.\n\n\"Available to consumers\" means an individual member of the public (not only enrolled enterprise
customers) can complete a purchase transaction. Region-locked launches (e.g., China-only or US-only first wave) count. Listings that immediately sell out also count, provided actual orders were
accepted.", "num_forecasters": 6, "community_prediction": null}
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "Nvidia N1 N1X ARM SoC Windows PC Computex 2026 announcement availability launch date",
      "ttl": "6h"
    },
    {
      "query": "Nvidia N1 N1X laptop OEM Dell Lenovo availability pre-order purchase date June 2026",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Nvidia N1 N1X ARM SoC Windows PC Computex 2026 announcement availability launch date", "entry": {"slug": "nvidia-n1-n1x-arm-soc-windows-pc-computex-2026-ann-64377b15", "query":
"Nvidia N1 N1X ARM SoC Windows PC Computex 2026 announcement availability launch date", "answer": "This is an excellent and comprehensive report from the research agent. Let me compile the final
synthesis.\n\n---\n\n# Nvidia N1 / N1X ARM SoC \u2014 Computex 2026 Research Report\n\n## Executive Summary\n\nOn **June 1, 2026**, at Computex 2026 (GTC Taipei Day Zero), Nvidia CEO Jensen Huang
officially unveiled the **RTX Spark Superchip** \u2014 the consumer branding for what was previously known as the N1X ARM SoC. Co-developed with MediaTek, this chip combines ARM CPU cores (Cortex-X925
+ A725) with Nvidia's Blackwell GPU architecture and up to 128GB of unified LPDDR5X memory. Over 30 laptops and ~10 desktops were announced from major OEMs, with systems arriving **Fall
2026**.\n\n---\n\n## 1. Announcement Timeline\n\n- **January 2025 (CES 2025):** Nvidia announced \"Project DIGITS\" with MediaTek, revealing the GB10 \"Superchip\" \u2014 the basis for N1/N1X.\n-
**May 2025 (Computex 2025):** Expected unveil did NOT happen; Nvidia shied away from announcing the chips.\n- **June 10, 2025:** N1X appeared on Geekbench (20-core, HP dev board, Linux), scoring 3,096
single-core / 18,837 multi-core.\n- **September 19, 2025:** Jensen Huang confirmed N1 and GB10 are identical silicon.\n- **January 20, 2026:** Digitimes reported Nvidia preparing multiple ARM chips
for 2026-2027; N1X laptops expected with Windows 11 26H1.\n- **April 9, 2026:** Images of N1/N1X laptop motherboard with 128GB LPDDR5X surfaced on Goofish (Chinese platform), listed at $1,400 / 9,999
RMB.\n- **May 29, 2026:** Nvidia and Microsoft both posted \"A new era of PC\" on social media, teasing the Computex reveal.\n- **May 31, 2026:** Full spec sheet leaked via VideoCardz.\n- **June 1,
2026 (Computex 2026):** Official unveil as **\"RTX Spark Superchip\"**. Systems shipping **Fall 2026**.\n\n---\n\n## 2. Specifications\n\n### N1X (High-End \u2014 \"RTX Spark Superchip\")\n\n| Spec |
Top SKU | Lower SKU |\n|------|---------|-----------|\n| **CPU Cores** | 20 (10P + 10E) | 18 (9P + 9E) |\n| **CPU Architecture** | ARM Cortex-X925 + A725 (Grace) | Same |\n| **GPU CUDA Cores** | 6,144
(= RTX 5070) | 5,120 |\n| **GPU Architecture** | Blackwell | Blackwell |\n| **Memory** | Up to 128GB LPDDR5X, 16-channel | Same |\n| **Memory Bandwidth** | Up to 300 GB/s | Same |\n| **TDP** |
45W\u201380W | 45W\u201380W |\n| **Process** | TSMC 3nm-class | Same |\n| **AI Compute** | Up to 1 PFLOP | \u2014 |\n| **PCIe** | 12x PCIe 5.0 + 5x PCIe 4.0 | Same |\n| **Interconnect** | NVLink C2C
(CPU\u2194GPU) | Same |\n\n### N1 (Mainstream)\n\n| Spec | Top SKU | Lower SKU |\n|------|---------|-----------|\n| **CPU Cores** | 12 (8P + 4E) | 10 (7P + 3E) |\n| **GPU CUDA Cores** | 2,560 | 2,048
|\n| **Memory** | Up to 64GB LPDDR5X, 8-channel | Same |\n| **TDP** | 18W\u201345W | 18W\u201345W |\n| **PCIe** | 8x PCIe 5.0 + 3x PCIe 4.0 | Same |\n\n---\n\n## 3. Availability / Launch Date\n\n-
**Official availability: Fall 2026** (announced June 1, 2026 at Computex).\n- Originally expected late 2025, pushed to 2026 due to: (1) Windows 11 26H1 OS timing, (2) uncertain notebook demand, (3)
LPDDR5X memory supply/pricing (\"RAM crisis\").\n- **Next-gen N2/N2X chips** planned for **Q3 2027**.\n\n---\n\n## 4. OEM Partners\n\n**Fall 2026 Launch Partners:**\n- ASUS, Dell, HP, Lenovo,
**Microsoft** (Surface Laptop Ultra), MSI\n\n**To Follow:**\n- Acer, GIGABYTE\n\n**Microsoft Surface Laptop Ultra** highlights:\n- 15-inch mini-LED PixelSense Ultra (2880\u00d71920, 2000 nits HDR)\n-
Full N1X: 20 ARM cores, 6,144 CUDA cores, 128GB unified LPDDR5X\n- Under 4.5 lbs; Platinum and Nightfall colors\n\n---\n\n## 5. Comparison vs. Qualcomm Snapdragon X Elite\n\n| Metric | Nvidia N1X |
Snapdragon X Elite |\n|--------|------------|-------------------|\n| **Single-Core (GB6)** | 3,096 | 2,693 |\n| **Multi-Core (GB6)** | 18,837 | 13,950 |\n| **GPU** | 6,144 CUDA cores (Blackwell) |
Adreno (poor driver quality) |\n| **Max Memory** | 128GB LPDDR5X | 32GB |\n| **CPU Architecture** | Cortex-X925/A725 | Oryon V1 |\n\nN1X is ~15% faster single-core and ~35% faster multi-core than
Snapdragon X Elite, with a vastly superior GPU. Qualcomm moved ~720K Snapdragon X units in Q3 2024 (~0.8% PC market share). Qualcomm's exclusive Windows on ARM deal with Microsoft expired in
2024.\n\n---\n\n## 6. Computex 2026 Key Reveals\n\n1. **RTX Spark Superchip** official branding and full lineup (4 SKUs)\n2. **\"Agentic AI OS\"** vision \u2014 Windows transformed for AI agents\n3.
**100+ FPS 1440p gaming** via DLSS 4.5 and Multi Frame Generation\n4. **Anti-cheat/DRM support** \u2014 Easy Anti-Cheat, BattlEye, Denuvo natively on ARM64\n5. **Adobe partnership** \u2014 Photoshop
rebuilt as 100% GPU-accelerated for RTX Spark\n6. **OpenShell framework** \u2014 Nvidia/Microsoft AI agent security framework\n7. **120B-parameter LLM** capability with 1M tokens of context
locally\n8. **RTX Spark roadmap** \u2014 Blackwell \u2192 Blackwell Ultra \u2192 Rubin\n9. **DLSS 5** also announced\n\n---\n\n## 7. Pricing\n\n- **No official consumer pricing announced yet.**\n- DGX
Spark (GB10/Linux): $3,999 baseline, approaching $5,000 due to RAM pricing.\n- N1X laptops expected to target **$2,000+** (MacBook Pro competitor).\n- N1 mainstream laptops could be under
**$1,500**.\n- RAM crisis and TSMC 3nm costs point toward premium pricing.\n\n---\n\n## 8. MediaTek Partnership\n\n- MediaTek co-developed the CPU; Nvidia handles the GPU and software stack.\n- CPU
uses off-the-shelf ARM Cortex-X925 (performance) + A725 (efficiency) cores.\n- Partnership began with GB10 for DGX Spark and extended to consumer RTX Spark.\n- MediaTek secured large FCBGA packaging
capacity in late 2024, implying high-volume production.\n- Jensen Huang described the CPU as \"half engineered by smartphone SoC vendor MediaTek.\"\n\n---", "sources": [{"url":
"https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-
memory", "title": "Nvidia Unveils RTX Spark Superchip at Computex 2026", "domain": "tomshardware.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Nvidia CEO Jensen Huang officially unveiled
the RTX Spark Superchip at Computex 2026 with ARM CPU, Blackwell GPU, and 128GB unified memory. Over 30 laptops and ~10 desktops announced for Fall 2026."}, {"url": "https://www.tomshardware.com/pc-
components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs", "title": "Nvidia N1/N1X
SoC Specs Leak Ahead of Computex Launch", "domain": "tomshardware.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Full spec sheet leaked May 31, 2026: N1X with 20 cores and 6,144 CUDA cores;
N1 with 10-12 cores and 2,048-2,560 CUDA cores."}, {"url": "https://www.tomshardware.com/laptops/nvidia-and-microsoft-tease-a-new-era-of-pc-ahead-of-computex-2026-coordinated-social-media-posts-could-
indicate-that-rumored-n1x-laptops-will-be-windows-on-arm-systems", "title": "Nvidia and Microsoft Tease 'A New Era of PC' Ahead of Computex 2026", "domain": "tomshardware.com", "accessed_at":
"2026-06-02T00:00:00Z", "snippet": "May 29, 2026: Nvidia and Microsoft both posted 'A new era of PC' on social media with coordinates pointing to Computex 2026 keynote venue."}, {"url":
"https://www.tomshardware.com/pc-components/cpus/nvidia-ceo-huang-says-upcoming-dgx-spark-systems-are-powered-by-n1-silicon-confirms-gb10-superchip-and-n1-n1x-socs-are-identical", "title": "Nvidia CEO
Confirms GB10 and N1/N1X SoCs Are Identical", "domain": "tomshardware.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "September 19, 2025: Jensen Huang confirmed N1 and GB10 are identical
silicon, with N1 going into DGX Spark and other products."}, {"url": "https://www.tomshardware.com/pc-components/cpus/nvidias-20-core-n1x-leaks-with-3000-single-core-geekbench-score-arm-chip-could-
rival-intel-and-amds-laptop-offerings", "title": "Nvidia N1X Leaks with 3000 Single-Core Geekbench Score", "domain": "tomshardware.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "June 10,
2025: N1X appeared on Geekbench with 20 cores, scoring 3,096 single-core and 18,837 multi-core on HP development board."}, {"url": "https://www.windowslatest.com/2026/01/20/report-nvidia-prepares-
multiple-arm-based-chips-for-2026-and-2027-first-gen-could-debut-with-windows-11-26h1/", "title": "Report: Nvidia Prepares Multiple ARM-Based Chips for 2026 and 2027", "domain": "windowslatest.com",
"accessed_at": "2026-06-02T00:00:00Z", "snippet": "January 20, 2026: Digitimes sources report Nvidia preparing ARM chips for 2026-2027, with N1X laptops expected with Windows 11 26H1."}, {"url":
"https://www.tomshardware.com/pc-components/motherboards/alleged-images-of-the-long-awaited-nvidia-n1-n1x-soc-surface-on-laptop-motherboard-board-features-128-gb-of-lpddr5x-memory-
alongside-8-6-2-phase-vrm", "title": "Alleged Images of Nvidia N1/N1X SoC Surface on Laptop Motherboard", "domain": "tomshardware.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "April 9,
2026: N1/N1X laptop motherboard with 128GB LPDDR5X spotted on Goofish for $1,400 (9,999 RMB)."}, {"url": "https://www.tomshardware.com/laptops/microsoft-surface-laptop-ultra-weilds-nvidias-rtx-spark-
superchip-with-128gb-of-ram-20-arm-cpu-cores-and-a-blackwell-gpu-15-inch-mini-led-pixelsense-ultra-display-rounds-out-the-powerful-package", "title": "Microsoft Surface Laptop Ultra with RTX Spark
Superchip", "domain": "tomshardware.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Surface Laptop Ultra: 15-inch mini-LED, 2880x1920, 2000 nits, 20 ARM cores, 6144 CUDA cores, 128GB unified
RAM, under 4.5 lbs."}, {"url": "https://www.tomshardware.com/pc-components/cpus/nvidia-says-rtx-spark-chip-will-support-all-major-anti-cheat-and-drm-technologies-fortnite-valorant-denuvo-and-more-to-
work-natively-with-windows-on-arm", "title": "Nvidia RTX Spark to Support All Major Anti-Cheat and DRM Technologies", "domain": "tomshardware.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet":
"Easy Anti-Cheat, BattlEye, Denuvo confirmed for native ARM64 support on RTX Spark."}, {"url": "https://www.tomshardware.com/pc-components/cpus/nvidia-lays-out-rtx-spark-roadmap-for-laptops-and-
desktop-pcs-at-computex-2026", "title": "Nvidia Lays Out RTX Spark Roadmap at Computex 2026", "domain": "tomshardware.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Three generations
planned: Blackwell, Blackwell Ultra, Rubin. N2/N2X chips planned for Q3 2027."}, {"url": "https://en.wikipedia.org/wiki/Nvidia_N1", "title": "Nvidia N1 - Wikipedia", "domain": "en.wikipedia.org",
"accessed_at": "2026-06-02T00:00:00Z", "snippet": "Wikipedia article on Nvidia N1 ARM SoC co-developed with MediaTek."}, {"url": "https://www.tomshardware.com/laptops/nvidia-enters-the-windows-pc-
market-with-rtx-spark", "title": "Nvidia Enters the Windows PC Market with RTX Spark", "domain": "tomshardware.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Analysis comparing RTX Spark to
Qualcomm Snapdragon X Elite. Qualcomm moved ~720K units in Q3 2024 (~0.8% PC share)."}], "key_facts": ["Nvidia officially unveiled the 'RTX Spark Superchip' (formerly known as N1X) at Computex 2026
(GTC Taipei Day Zero) on June 1, 2026.", "RTX Spark systems (laptops and desktops) will be available in Fall 2026 from OEM partners including ASUS, Dell, HP, Lenovo, Microsoft, and MSI, with Acer and
GIGABYTE to follow.", "The N1X top SKU features 20 ARM CPU cores (10 Cortex-X925 + 10 Cortex-A725), 6,144 Blackwell CUDA cores (matching desktop RTX 5070), and up to 128GB unified LPDDR5X memory.",
"The mainstream N1 SKU features 10-12 ARM cores, 2,048-2,560 CUDA cores, up to 64GB LPDDR5X, and 18W-45W TDP \u2014 targeting sub-$1,500 laptops.", "N1X TDP ranges from 45W to 80W; manufactured on
TSMC 3nm-class process.", "N1X outperforms Qualcomm Snapdragon X Elite by ~15% single-core and ~35% multi-core in Geekbench 6 benchmarks.", "Microsoft announced Surface Laptop Ultra as a flagship RTX
Spark device with 15-inch mini-LED display, 128GB RAM, and under 4.5 lbs.", "MediaTek co-developed the CPU side; Nvidia handles GPU (Blackwell) and software stack. NVLink C2C connects CPU and GPU.",
"Nvidia claims RTX Spark can run 120B-parameter LLMs with 1M tokens of context locally and deliver 100+ FPS 1440p gaming via DLSS 4.5.", "Anti-cheat and DRM support confirmed for ARM64: Easy Anti-
Cheat, BattlEye, Denuvo \u2014 enabling Fortnite, Valorant, Rocket League natively.", "No official consumer pricing announced; N1X laptops expected at $2,000+, N1 laptops under $1,500. LPDDR5X memory
crisis is inflating costs.", "Next-generation N2/N2X chips are planned for Q3 2027; RTX Spark roadmap spans Blackwell \u2192 Blackwell Ultra \u2192 Rubin.", "Qualcomm's exclusive Windows on ARM deal
with Microsoft expired in 2024, opening the door for Nvidia's entry.", "The chip was originally expected in late 2025 but was delayed due to Windows 11 26H1 timing, weak notebook demand, and memory
supply issues.", "Over 30 laptops and ~10 desktops announced across all OEM partners at Computex 2026."], "data_points": [{"metric": "N1X Top SKU CPU Cores", "value": 20.0, "unit": "cores (10P+10E)",
"as_of": "2026-06-01", "source_url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-
blackwell-gpu-and-128gb-unified-memory"}, {"metric": "N1X Top SKU CUDA Cores", "value": 6144.0, "unit": "CUDA cores", "as_of": "2026-06-01", "source_url": "https://www.tomshardware.com/pc-
components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs"}, {"metric": "N1X Max
Unified Memory", "value": 128.0, "unit": "GB LPDDR5X", "as_of": "2026-06-01", "source_url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-
promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory"}, {"metric": "N1X Memory Bandwidth", "value": 300.0, "unit": "GB/s", "as_of": "2026-06-01",
"source_url": "https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-
with-12-and-10-core-configs"}, {"metric": "N1X TDP Range", "value": 80.0, "unit": "watts (max)", "as_of": "2026-06-01", "source_url": "https://www.tomshardware.com/pc-components/cpus/nvidias-long-
awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs"}, {"metric": "N1X Geekbench 6 Single-Core Score",
"value": 3096.0, "unit": "points", "as_of": "2025-06-10", "source_url": "https://www.tomshardware.com/pc-components/cpus/nvidias-20-core-n1x-leaks-with-3000-single-core-geekbench-score-arm-chip-could-
rival-intel-and-amds-laptop-offerings"}, {"metric": "N1X Geekbench 6 Multi-Core Score", "value": 18837.0, "unit": "points", "as_of": "2025-06-10", "source_url": "https://www.tomshardware.com/pc-
components/cpus/nvidias-20-core-n1x-leaks-with-3000-single-core-geekbench-score-arm-chip-could-rival-intel-and-amds-laptop-offerings"}, {"metric": "Snapdragon X Elite Geekbench 6 Single-Core Score",
"value": 2693.0, "unit": "points", "as_of": "2025-06-10", "source_url": "https://www.tomshardware.com/pc-components/cpus/nvidias-20-core-n1x-leaks-with-3000-single-core-geekbench-score-arm-chip-could-
rival-intel-and-amds-laptop-offerings"}, {"metric": "Snapdragon X Elite Geekbench 6 Multi-Core Score", "value": 13950.0, "unit": "points", "as_of": "2025-06-10", "source_url":
"https://www.tomshardware.com/pc-components/cpus/nvidias-20-core-n1x-leaks-with-3000-single-core-geekbench-score-arm-chip-could-rival-intel-and-amds-laptop-offerings"}, {"metric": "N1X AI Compute
Performance", "value": 1.0, "unit": "petaflops", "as_of": "2026-06-01", "source_url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-
to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory"}, {"metric": "N1 Mainstream Max CPU Cores", "value": 12.0, "unit": "cores (8P+4E)", "as_of": "2026-06-01",
"source_url": "https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-
with-12-and-10-core-configs"}, {"metric": "N1 Mainstream Max CUDA Cores", "value": 2560.0, "unit": "CUDA cores", "as_of": "2026-06-01", "source_url": "https://www.tomshardware.com/pc-
components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs"}, {"metric": "N1 Mainstream
TDP Range", "value": 45.0, "unit": "watts (max)", "as_of": "2026-06-01", "source_url": "https://www.tomshardware.com/pc-components/cpus/nvidias-long-awaited-n1-n1x-soc-specs-leak-ahead-of-computex-
launch-n1-to-feature-up-to-20-arm-based-cores-standard-n1-equipped-with-12-and-10-core-configs"}, {"metric": "OEM Laptops Announced", "value": 30.0, "unit": "laptop models", "as_of": "2026-06-01",
"source_url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-
and-128gb-unified-memory"}, {"metric": "OEM Desktops Announced", "value": 10.0, "unit": "desktop models", "as_of": "2026-06-01", "source_url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-
spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory"}, {"metric": "Qualcomm Snapdragon X Q3 2024 Unit
Shipments", "value": 720000.0, "unit": "units", "as_of": "2024-09-30", "source_url": "https://www.tomshardware.com/laptops/nvidia-enters-the-windows-pc-market-with-rtx-spark"}, {"metric": "Qualcomm
Snapdragon X PC Market Share Q3 2024", "value": 0.8, "unit": "percent", "as_of": "2024-09-30", "source_url": "https://www.tomshardware.com/laptops/nvidia-enters-the-windows-pc-market-with-rtx-spark"},
{"metric": "DGX Spark Baseline Price", "value": 3999.0, "unit": "USD", "as_of": "2026-04-09", "source_url": "https://www.tomshardware.com/pc-components/motherboards/alleged-images-of-the-long-awaited-
nvidia-n1-n1x-soc-surface-on-laptop-motherboard-board-features-128-gb-of-lpddr5x-memory-alongside-8-6-2-phase-vrm"}, {"metric": "N1X Max LLM Parameter Count (local)", "value": 120.0, "unit": "billion
parameters", "as_of": "2026-06-01", "source_url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-
with-arm-cpu-blackwell-gpu-and-128gb-unified-memory"}, {"metric": "Surface Laptop Ultra Display Resolution", "value": 2880.0, "unit": "x 1920 pixels", "as_of": "2026-06-01", "source_url":
"https://www.tomshardware.com/laptops/microsoft-surface-laptop-ultra-weilds-nvidias-rtx-spark-superchip-with-128gb-of-ram-20-arm-cpu-cores-and-a-blackwell-gpu-15-inch-mini-led-pixelsense-ultra-
display-rounds-out-the-powerful-package"}, {"metric": "Surface Laptop Ultra Peak HDR Brightness", "value": 2000.0, "unit": "nits", "as_of": "2026-06-01", "source_url":
"https://www.tomshardware.com/laptops/microsoft-surface-laptop-ultra-weilds-nvidias-rtx-spark-superchip-with-128gb-of-ram-20-arm-cpu-cores-and-a-blackwell-gpu-15-inch-mini-led-pixelsense-ultra-
display-rounds-out-the-powerful-package"}], "created_at": "2026-06-02T01:33:33.111181Z", "updated_at": "2026-06-02T01:33:33.111181Z", "stale_after": "2026-06-02T07:33:33.111181Z", "state": "fresh",
"revision_history": [], "session_id": "2abc9d40-9203-4a3b-a6cd-bd6d2baa24ec", "follow_up_count": 0}, "is_follow_up": false}, {"query": "Nvidia N1 N1X laptop OEM Dell Lenovo availability pre-order
purchase date June 2026", "entry": {"slug": "nvidia-n1-n1x-laptop-oem-dell-lenovo-availability-9b56ba25", "query": "Nvidia N1 N1X laptop OEM Dell Lenovo availability pre-order purchase date June
2026", "answer": "I have comprehensive findings from the first research task. Here is my full synthesis:\n\n---\n\n# Nvidia N1 / N1X (RTX Spark) Laptop Availability \u2014 Research Report\n\n##
Overview\n\nThe Nvidia \"N1\" and \"N1X\" are internal chip designations for what Nvidia officially branded as the **NVIDIA RTX Spark** family. These are ARM-based laptop/desktop processors combining
Nvidia's Grace CPU and Blackwell RTX GPU architectures on a single chip, manufactured at TSMC's 3nm node in partnership with MediaTek. They were **announced on June 1, 2026** at Nvidia's GTC Taipei
keynote during Computex 2026.\n\n## Key Specifications\n\n- **CPU:** Custom 20-core Grace ARM CPU (built with MediaTek, connected via NVLink)\n- **GPU:** Blackwell RTX with 6,144 CUDA cores (~RTX 5070
Laptop equivalent)\n- **AI Performance:** 1 petaflop\n- **Memory:** Up to 128GB unified LPDDR5X (lower tiers down to 16GB)\n- **Process:** TSMC 3nm\n- **Power:** Scales from low single-digit watts up
to 80W\n\n## Confirmed OEM Laptops (8 at launch)\n\n| OEM | Model |\n|-----|-------|\n| **Dell** | **XPS 16** |\n| **Lenovo** | **Yoga Pro 9n** |\n| **Microsoft** | Surface Laptop Ultra |\n| **Asus**
| ProArt P14 and ProArt P16 |\n| **HP** | OmniBook X 14 and OmniBook Ultra 16 |\n| **MSI** | Prestige N16 Flip AI Plus |\n\nAdditional partners Acer and Gigabyte have unnamed models in development.
Nvidia says **30+ laptops and 10+ desktops** are in the pipeline.\n\n## Availability & Pre-Order Status (as of June 2, 2026)\n\n- **Announcement date:** June 1, 2026\n- **Expected launch:** **Fall
2026** (no specific month)\n- **Pre-orders:** **NOT yet available** \u2014 no pre-order dates have been announced by any OEM\n- **Current status:** Just announced; zero benchmarks or comparative
performance data shared\n- Nvidia says more details (benchmarks, pricing, exact dates) will come \"closer to launch\"\n\n## Pricing\n\n- **No official prices announced** from any OEM\n- Nvidia
described the initial launch as targeting **\"premium price points\"**\n- Analysts and press estimate the range at **$2,000\u2013$2,500+** for initial models\n- Comparable reference points:\n  - DGX
Spark desktop (same GB10 silicon): ~$4,700\n  - AMD Strix Halo 128GB laptops: $3,000\u2013$3,300\n- Lower-cost RTX Spark variants (as little as 16GB RAM) are planned for later\n\n## Software Ecosystem
Readiness\n\n- Adobe rearchitecting Photoshop/Premiere for RTX Spark (claiming 2x AI/graphics speedup)\n- Microsoft preparing Windows security primitives for AI agents\n- Games with anti-cheat
(Valorant, LoL, PUBG, Fortnite) adding Windows on ARM support\n- Full CUDA-X software stack claimed to run on RTX Spark\n- No Linux driver support confirmed\n\n## Key Unknowns\n\n- Exact launch dates
and pre-order windows for Dell XPS 16 and Lenovo Yoga Pro 9n\n- Specific pricing from any OEM\n- Performance benchmarks vs. Intel, AMD, Apple, or Qualcomm\n- Manufacturing location (Nvidia declined to
comment)\n- Detailed specs (screen, battery, storage) for individual OEM models\n\n---\n\n**Bottom line for June 2026:** The Dell XPS 16 and Lenovo Yoga Pro 9n with Nvidia RTX Spark (N1/N1X) chips
have been **announced but are not available for purchase or pre-order**. The expected availability window is **fall 2026**, with no specific dates or pricing disclosed yet.\n\n---\n\n**Sources:**\n-
Nvidia GTC Taipei at Computex 2026 blog: https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/\n- The Verge \u2014 RTX Spark announcement (Sean Hollister, June 1, 2026):
https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date\n- The Verge \u2014 First confirmed RTX Spark laptops (June 1, 2026):
https://www.theverge.com/tech/940587/these-are-the-first-confirmed-nvidia-rtx-spark-laptops\n- The Verge \u2014 Pricing/M1 comparison analysis (Antonio G. Di Benedetto, June 1, 2026):
https://www.theverge.com/tech/941215/windows-laptops-nvidia-rtx-spark-apple-m1-arm-price-ram\n- Microsoft Surface Laptop Ultra announcement: https://www.theverge.com/tech/940584/microsoft-surface-
laptop-ultra-nvidia-rtx-spark-pictures", "sources": [{"url": "https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/", "title": "Nvidia GTC Taipei at Computex 2026 Official Blog",
"domain": "blogs.nvidia.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Official Nvidia blog post covering GTC Taipei announcements including RTX Spark chip family and OEM partnerships."},
{"url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date", "title": "Nvidia RTX Spark N1/N1X Laptop Desktop PC CPU GPU AI Release Date",
"domain": "theverge.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Sean Hollister's comprehensive article on RTX Spark announcement, specs (20-core Grace CPU, 6144 CUDA cores, 1 petaflop AI,
up to 128GB LPDDR5X), and fall 2026 launch window."}, {"url": "https://www.theverge.com/tech/940587/these-are-the-first-confirmed-nvidia-rtx-spark-laptops", "title": "These Are the First Confirmed
Nvidia RTX Spark Laptops", "domain": "theverge.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Lists all 8 confirmed launch laptops: Dell XPS 16, Lenovo Yoga Pro 9n, Microsoft Surface Laptop
Ultra, Asus ProArt P14/P16, HP OmniBook X 14/Ultra 16, MSI Prestige N16 Flip AI Plus."}, {"url": "https://www.theverge.com/tech/941215/windows-laptops-nvidia-rtx-spark-apple-m1-arm-price-ram",
"title": "Windows Laptops Nvidia RTX Spark Apple M1 ARM Price RAM Analysis", "domain": "theverge.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Analysis comparing RTX Spark launch strategy
to Apple M1, noting premium pricing focus ($2000-2500+ estimated) and concern about launching at high price points first."}, {"url": "https://www.theverge.com/tech/940584/microsoft-surface-laptop-
ultra-nvidia-rtx-spark-pictures", "title": "Microsoft Surface Laptop Ultra Nvidia RTX Spark Announcement", "domain": "theverge.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Microsoft
Surface Laptop Ultra with RTX Spark, described by Surface boss Andrew Hill as 'the most powerful thing we've ever made.'"}], "key_facts": ["Nvidia N1/N1X are internal chip designations for the
officially branded 'NVIDIA RTX Spark' family of ARM-based processors, announced June 1, 2026 at GTC Taipei / Computex 2026.", "RTX Spark combines a 20-core Grace ARM CPU with a Blackwell RTX GPU
(6,144 CUDA cores) on a single TSMC 3nm chip, built in partnership with MediaTek.", "The chip delivers 1 petaflop of AI performance with up to 128GB unified LPDDR5X memory, scaling from low single-
digit watts to 80W.", "Dell XPS 16 and Lenovo Yoga Pro 9n are among 8 confirmed launch laptops with RTX Spark chips.", "Other confirmed OEM laptops: Microsoft Surface Laptop Ultra, Asus ProArt
P14/P16, HP OmniBook X 14 / OmniBook Ultra 16, MSI Prestige N16 Flip AI Plus.", "Over 30 laptops and 10 desktops with RTX Spark are in development across OEMs including Acer and Gigabyte.", "As of
June 2, 2026, NO pre-orders are available from any OEM \u2014 the products were just announced on June 1, 2026.", "Expected launch window is Fall 2026, with no specific month or date disclosed.", "No
official pricing has been announced; Nvidia describes initial launch as targeting 'premium price points' \u2014 analysts estimate $2,000\u2013$2,500+.", "Lower-cost RTX Spark variants with as little
as 16GB RAM are planned for after the initial premium launch.", "Nvidia has shared zero performance benchmarks vs. Intel, AMD, Apple, or Qualcomm \u2014 details promised 'closer to launch'.", "GPU
performance is roughly equivalent to an RTX 5070 Laptop GPU.", "Adobe is rearchitecting Photoshop and Premiere for RTX Spark; full CUDA-X stack is claimed to run on the platform.", "No Linux driver
support has been confirmed; focus is on Windows only."], "data_points": [{"metric": "RTX Spark Grace CPU cores", "value": 20.0, "unit": "cores", "as_of": "2026-06-01", "source_url":
"https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date"}, {"metric": "RTX Spark Blackwell GPU CUDA cores", "value": 6144.0, "unit": "CUDA cores",
"as_of": "2026-06-01", "source_url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date"}, {"metric": "RTX Spark AI performance", "value": 1.0,
"unit": "petaflop", "as_of": "2026-06-01", "source_url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date"}, {"metric": "Maximum unified LPDDR5X
memory", "value": 128.0, "unit": "GB", "as_of": "2026-06-01", "source_url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date"}, {"metric":
"Minimum planned memory tier", "value": 16.0, "unit": "GB", "as_of": "2026-06-01", "source_url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-
date"}, {"metric": "Maximum TDP", "value": 80.0, "unit": "watts", "as_of": "2026-06-01", "source_url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-
release-date"}, {"metric": "Confirmed launch laptops", "value": 8.0, "unit": "models", "as_of": "2026-06-01", "source_url": "https://www.theverge.com/tech/940587/these-are-the-first-confirmed-nvidia-
rtx-spark-laptops"}, {"metric": "Total RTX Spark laptops in development", "value": 30.0, "unit": "models (30+)", "as_of": "2026-06-01", "source_url": "https://www.theverge.com/tech/940587/these-are-
the-first-confirmed-nvidia-rtx-spark-laptops"}, {"metric": "Total RTX Spark desktops in development", "value": 10.0, "unit": "models (10+)", "as_of": "2026-06-01", "source_url":
"https://www.theverge.com/tech/940587/these-are-the-first-confirmed-nvidia-rtx-spark-laptops"}, {"metric": "Estimated premium laptop price floor", "value": 2000.0, "unit": "USD", "as_of":
"2026-06-01", "source_url": "https://www.theverge.com/tech/941215/windows-laptops-nvidia-rtx-spark-apple-m1-arm-price-ram"}, {"metric": "DGX Spark desktop price (same GB10 chip)", "value": 4700.0,
"unit": "USD", "as_of": "2026-06-01", "source_url": "https://www.theverge.com/tech/940589/nvidia-rtx-spark-n1-n1x-laptop-desktop-pc-cpu-gpu-ai-release-date"}], "created_at":
"2026-06-02T01:34:17.228109Z", "updated_at": "2026-06-02T01:34:17.228109Z", "stale_after": "2026-06-02T07:34:17.228109Z", "state": "fresh", "revision_history": [], "session_id":
"c3a09695-94b9-4a49-adfb-beca9244d9f1", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 2, "failed_count": 0}
```

## 💬 Response

The research is comprehensive. Let me now check for any surprise same-day availability announcements and look at historical precedents for Computex-to-retail timelines.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Nvidia RTX Spark N1X laptop pre-order buy now available June 2026"
}
```

### 📋 Result

```
{"query": "Nvidia RTX Spark N1X laptop pre-order buy now available June 2026", "results": [{"title": "Nvidia N1X officially confirmed to arrive as the RTX Spark - Notebookcheck News", "url":
"https://www.notebookcheck.net/Nvidia-N1X-officially-confirmed-to-arrive-as-the-RTX-Spark.1312010.0.html", "snippet": "The Nvidia RTX Spark has officially been shown off at Computex
2026\nNvidia\u2019s first consumer-grade laptop chip, the RTX Spark, is finally here. It is essentially a modified version of the DGX Spark launched last year, but with Windows support.\nNvidia\u2019s
long-awaited Windows on ARM chip is finally here. It is made on an unspecified 3 nm node from TSMC. Formerly known as the N1X, which was likely its internal codename, the chip will launch as the RTX
Spark. It won\u2019t be the only one, with Nvidia stat", "api_data": null, "hint": null}, {"title": "NVIDIA RTX Spark \u2014 Slim Laptops & Small Desktops", "url": "https://www.nvidia.com/en-
us/products/rtx-spark/", "snippet": "RTX Spark Superchip\nUp to\nBlackwell RTX GPU\nUp to\nUltra-Efficient CPU\nUp to\nFP4 AI Performance\nUp to\nUnified Memory\nCUDA, the software that accelerates
the world\u2019s AI, runs natively on RTX Spark.\nThe most power-efficient RTX chip ever made, in a chassis so slim you'll forget you\u2019re carrying it.\nMake a million ideas happen with hundreds of
creative apps and AI tools supercharged by RTX and [NVIDIA Studio](https://www.nvidia.com/en-us/studio/) tools.\nPlay the latest and greatest games with world-l", "api_data": null, "hint": null},
{"title": "HP unveils world's thinnest RTX Spark laptops: 12K video editing, 128GB RAM, all-day battery - Notebookcheck News", "url": "https://www.notebookcheck.net/HP-unveils-world-s-thinnest-RTX-
Spark-laptops-12K-video-editing-128GB-RAM-all-day-battery.1312200.0.html", "snippet": "HP just announced the OmniBook Ultra 16 and OmniBook X 14, the world\u2019s thinnest laptops powered by the new
Nvidia RTX Spark superchip. Featuring up to 128GB of unified memory and Blackwell GPU architecture, these next-gen AI PCs are designed to run complex local agents and advanced creative workflows for
developers and power users, launching later in 2026.\nIn addition to the new OmniDesk Mini Desktop PC, dubbed as the \"world's first AI mini PC\", HP wants to redefine the thin-and-light laptop cat",
"api_data": null, "hint": null}, {"title": "Nvidia unveils RTX Spark computer chip with up to 20 cores, RTX 5070 GPU and 128GB RAM - GSMArena.com news", "url":
"https://www.gsmarena.com/nvidia_unveils_rtx_spark_computer_chip_with_up_to_20_cores_rtx_5070__128gb_ram-news-73061.php", "snippet": "Nvidia took the stage at Computex 2026 for its highly awaited
entry into the consumer chip market - meet the RTX Spark, a chipset that merges a powerful and efficient ARM CPU with an RTX GPU.\nThe RTX Spark superchip merges an Nvidia Grace CPU with up to 20
cores with an Nvidia Blackwell GPU with 6,144 CUDA cores, and up to 128GB of fast, LPDDR5X unified memory.\nThe processor is based on Nvidia's GB10 chip inside the DGX Spark platform, a class of
enterprise-aimed mini-PCs running a custom Ubuntu", "api_data": null, "hint": null}, {"title": "NVIDIA's RTX Spark is an AI \"superchip\" that will power Windows laptops and desktops - Engadget",
"url": "https://www.engadget.com/2184558/nvidia-rtx-spark-chip-windows-pcs/", "snippet": "NVIDIA's RTX Spark is an AI \"superchip\" that will power Windows laptops and desktops\nThe company claims it
offers 1 petaflop of AI computing power.\nIt was only a matter of time before NVIDIA released a powerful system-on-a-chip (SOC) to take on [AMD's Ryzen AI Max](https://www.engadget.com/computing/amds-
new-ryzen-ai-max-chips-and-ryzen-7-9850x3d-court-desktop-enthusiasts-at-ces-2026-033000587.html) and [Qualcomm's latest Snapdragon X2 chips](https://www.engadget.com/computing/qualcomm-says-its-",
"api_data": null, "hint": null}, {"title": "Introducing Surface Laptop Ultra: Made for world makers | Microsoft Devices Blog", "url": "https://blogs.windows.com/devices/2026/05/31/introducing-surface-
laptop-ultra-made-for-world-makers/", "snippet": "Introducing Surface Laptop Ultra: Made for world makers\nThe world is full of makers. Only a few make the world.\nSurface Laptop Ultra is for
them.\nFor those building the systems, the breakthroughs and the infrastructure the world runs on and gets changed by. The ones who see limits as flaws and have the vision to push past them.\nSurface
Laptop Ultra is the most powerful Surface Laptop ever built. Engineered with NVIDIA from the silicon up, optimized for RTX Spark, [built on Windows](https://blogs", "api_data": null, "hint": null},
{"title": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs at Computex 2026 \u2014 three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman | Tom's Hardware",
"url": "https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman",
"snippet": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs at Computex 2026 \u2014 three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman\nAlong with its first-
generation RTX Spark platform for desktop and laptop PCs, Nvidia CEO Jensen Huang revealed the company's commitment to future generations of those platforms on its future roadmaps. The company is
committed to producing at least two additional generations of Spark platforms for its partners.\nBeyond the Grace Blackwell ", "api_data": null, "hint": null}, {"title": "Nvidia unveils RTX Spark
Superchip for laptops and desktop PCs at Computex 2026 \u2013 new platform promises to turn Windows into an agentic AI OS with Arm CPU, Blackwell GPU, and 128GB unified memory | Tom's Hardware",
"url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-
unified-memory", "snippet": "Nvidia unveils RTX Spark Superchip for laptops and desktop PCs at Computex 2026 \u2013 new platform promises to turn Windows into an agentic AI OS with Arm CPU, Blackwell
GPU, and 128GB unified memory\nNvidia is transforming Windows into an agentic AI platform at Computex 2026. During his keynote, CEO Jensen Huang revealed the RTX Spark: a Windows on Arm platform for
laptops powered by the company's RTX Spark Superchip. The company boldly claims that this platform is \u201cthe most efficient ever built,\u201d a", "api_data": null, "hint": null}, {"title": "Nvidia
jumps into PCs with new Arm-based chip debuting in laptops from Microsoft, Dell, HP", "url": "https://www.cnbc.com/2026/05/31/nvidias-new-chip-to-power-fresh-line-of-windows-laptops-by-dell-hp.html",
"snippet": "[Nvidia](https://www.cnbc.com/quotes/NVDA/) has emerged as the world's most valuable company by dominating the market for artificial intelligence chips in the data center. Now the company
is expanding its prowess to chips that will serve as the main processor for personal computers, entering an arena that's long been ruled by [Intel](https://www.cnbc.com/quotes/INTC/), [Advanced Micro
Devices](https://www.cnbc.com/quotes/AMD/), [Qualcomm](https://www.cnbc.com/quotes/QCOM/) and [Apple](https://ww", "api_data": null, "hint": null}, {"title": "HP Debuts PCs Built for the Next Wave of
Windows PC Experiences Powered by NVIDIA RTX Spark\u2122", "url": "https://www.hp.com/us-en/newsroom/press-releases/2026/computex.html", "snippet": "Press Release\nHP Debuts PCs Built for the Next
Wave of Windows PC Experiences Powered by NVIDIA RTX Spark\u2122\nUnified portfolio delivers pre\u2011configured tools and secure local processing to accelerate AI workflows for creators, developers,
and gamers\nJune 1, 2026\nTAIPEI, June 1, 2026 \u2014 Today, HP Inc. (NYSE: HPQ) announced its latest devices and solutions, designed to enable developers of all types to create new experiences using
AI.\nHP is previewing PCs powered by NVIDIA RTX Spark\u2122, bringing a reinv", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Computex 2026 laptop \"available now\" \"order now\" \"buy now\" RTX Spark"
}
```

### 📋 Result

```
{"query": "Computex 2026 laptop \"available now\" \"order now\" \"buy now\" RTX Spark", "results": [{"title": "ASUS Unveils Revolutionary ProArt PCs Powered by NVIDIA RTX Spark at Computex 2026 | ASUS
Pressroom - Official Global News & Updates", "url": "https://press.asus.com/news/press-releases/asus-proart-p16-p14-mini-pc-nvidia-rtx-spark-computex-2026/", "snippet": "ASUS Unveils Revolutionary
ProArt PCs Powered by NVIDIA RTX Spark at Computex 2026\nNew ProArt P16 & P14 laptops and ProArt Mini PC unlock next-generation creative workflows with NVIDIA\u2019s new RTX Spark, a new superchip
that reinvents Windows PCs for the era of personal AI agents.\n- Powered by NVIDIA RTX Spark: ASUS introduces ProArt P16, P14 and Mini PC powered by the world\u2019s first Windows PCs purpose-built
for personal agents, reinventing the next wave of Windows PC experiences\n- Unified memory ", "api_data": null, "hint": null}, {"title": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs
at Computex 2026 \u2014 three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman | Tom's Hardware", "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-
sparrk-roadmap-for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman", "snippet": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs at
Computex 2026 \u2014 three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman\nAlong with its first-generation RTX Spark platform for desktop and laptop PCs, Nvidia CEO Jensen
Huang revealed the company's commitment to future generations of those platforms on its future roadmaps. The company is committed to producing at least two additional generations of Spark platforms
for its partners.\nBeyond the Grace Blackwell ", "api_data": null, "hint": null}, {"title": "Nvidia Computex 2026 keynote as it happened: RTX Spark announced to take on Apple, Intel, and Qualcomm |
TechRadar", "url": "https://www.techradar.com/news/live/nvidia-computex-2026", "snippet": "Sign up with your email below to instantly access member features, newsletters and exclusive Insider
perks\nBy submitting your information, you confirm you are aged 16 or over,\nhave read our\nPrivacy Policy\nand agree to the\nTerms & Conditions. Geographical rules apply.\nWe're live at Nvidia's
Computex 2026 keynote, where CEO Jensen Huang will share his vision of the future for not just the company, but the computing industry as a whole.\nWhile the company used to be best known for creating
some of t", "api_data": null, "hint": null}, {"title": "NVIDIA Computex 2026 Keynote Live Coverage - ServeTheHome", "url": "https://www.servethehome.com/nvidia-computex-2026-keynote-live-coverage/",
"snippet": "Kicking off today is the annual Computex tradeshow in Taiwan. Home to countless system and device manufacturers, Computex is a cornucopia of consumer electronics, and these days is also
the biggest PC-centric show of the year. And even though it takes place in June, barely half-way through the year, the show routinely sets the stage for the consumer and server products set to launch
later in the year, in the tech industry\u2019s critical third and fourth quarters.\nThere are several major keynotes dur", "api_data": null, "hint": null}, {"title": "Computex 2026: Nvidia launches
RTX Spark, DLSS 4.5 Ray Reconstruction and more | KitGuru", "url": "https://www.kitguru.net/gaming/matthew-wilson/computex-2026-nvidia-launches-rtx-spark-dlss-4-5-ray-reconstruction-and-more/",
"snippet": "We are kicking off our Computex 2026 coverage with Leo's breakdown of Nvidia's keynote. As you may expect, AI was at the very top of Nvidia's presentation, but there were also some
GeForce-related announcements for gamers too. Perhaps the most revealing moment of the entire presentation came when Jensen remarked that \u2018a long time ago Nvidia used to be a GPU company\u2019
\u2013 a statement that says a great deal about where the company sees its future.\nWatch via YouTube below:\nThe biggest announcement fro", "api_data": null, "hint": null}, {"title": "New GeForce RTX
Partner Cards, Laptops, Desktops & G-SYNC Displays Unveiled At COMPUTEX 2026", "url": "https://www.nvidia.com/en-us/geforce/news/computex-2026-partner-product-showcase/", "snippet": "COMPUTEX is a
gigantic tech exhibition, held annually in Taipei, Taiwan. Last year, over 86,000 members of the tech industry attended, and this year the organizers are predicting there\u2019ll be even more, as
there are a record 6,000+ booths and 1,500+ exhibitors on the show floor.\nFor gamers and creators, our partners unveiled NVIDIA-powered products, including new GeForce RTX 50 Series graphics card
models, new pre-built PCs, new [GeForce RTX](https://www.nvidia.com/en-us/geforce/laptops/50-series", "api_data": null, "hint": null}, {"title": "NVIDIA and Microsoft Reinvent Windows PCs for the Age
of Personal AI | NVIDIA Newsroom", "url": "https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark", "snippet": "News Summary:\n- NVIDIA RTX Spark powers the world\u2019s
first Windows PCs purpose-built for personal agents, featuring 1 petaflop of AI performance, industry-leading power efficiency, full-stack NVIDIA AI and graphics technology, and up to 128GB of unified
memory.\n- NVIDIA and Microsoft collaborate to deliver a native Windows experience for personal agents, including new security primitives and NVIDIA OpenShell to run agents securely on primary
devices.\n- RTX Spark lets creators, AI developers and g", "api_data": null, "hint": null}, {"title": "Computex 2026 Day 1 LIVE \u2014 Nvidia RTX Spark tested, and can Dell XPS 13 beat MacBook Neo? |
Tom's Guide", "url": "https://www.tomsguide.com/news/live/computex-2026", "snippet": "For the fastest way to join Tom's Guide Club enter your email below. We'll send you a confirmation and sign you up
to our newsletter to keep you updated on all the latest news.\nJoin the Tom's Guide Club for quick access. Enter your email below and we'll send confirmation, and sign you up to our newsletter.\nBy
submitting your information, you confirm you are aged 16 or over,\nhave read our\nPrivacy Policy\nand agree to the\nTerms & Conditions. Geographical rules apply.\nComputex 2026 has officially ju",
"api_data": null, "hint": null}, {"title": "Nvidia unveils RTX Spark Superchip for laptops and desktop PCs at Computex 2026 \u2013 new platform promises to turn Windows into an agentic AI OS with Arm
CPU, Blackwell GPU, and 128GB unified memory | Tom's Hardware", "url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-
into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory", "snippet": "Nvidia unveils RTX Spark Superchip for laptops and desktop PCs at Computex 2026 \u2013 new platform promises to
turn Windows into an agentic AI OS with Arm CPU, Blackwell GPU, and 128GB unified memory\nNvidia is transforming Windows into an agentic AI platform at Computex 2026. During his keynote, CEO Jensen
Huang revealed the RTX Spark: a Windows on Arm platform for laptops powered by the company's RTX Spark Superchip. The company boldly claims that this platform is \u201cthe most efficient ever
built,\u201d a", "api_data": null, "hint": null}, {"title": "Microsoft Introduces Surface Laptop Ultra with NVIDIA RTX Spark at Computex 2026 | Technobezz", "url":
"https://www.technobezz.com/news/microsoft-introduces-surface-laptop-ultra-with-nvidia-rtx-spark-at-computex-2026", "snippet": "[Microsoft just announced the Surface Laptop
Ultra](https://blogs.windows.com/devices/2026/05/31/introducing-surface-laptop-ultra-made-for-world-makers/) at Computex 2026, and it kills the old playbook. This is not a thin-and-light for
email.\nIt is a 1-petaflop AI workstation in a sub-18 mm chassis, [co-engineered with NVIDIA](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark) around the newly
announced RTX Spark chip. The [RTX Spark silicon pairs a Blackwell RTX G", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "\"RTX Spark\" OR \"N1X\" laptop \"shipping\" OR \"pre-order\" OR \"available\" date 2026"
}
```

### 📋 Result

```
{"query": "\"RTX Spark\" OR \"N1X\" laptop \"shipping\" OR \"pre-order\" OR \"available\" date 2026", "results": [{"title": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs at Computex
2026 \u2014 three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman | Tom's Hardware", "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-
for-laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman", "snippet": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs at Computex 2026
\u2014 three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman\nAlong with its first-generation RTX Spark platform for desktop and laptop PCs, Nvidia CEO Jensen Huang revealed
the company's commitment to future generations of those platforms on its future roadmaps. The company is committed to producing at least two additional generations of Spark platforms for its
partners.\nBeyond the Grace Blackwell ", "api_data": null, "hint": null}, {"title": "Microsoft's Surface Laptop Ultra with Nvidia's RTX Spark is coming this fall - GSMArena.com news", "url":
"https://www.gsmarena.com/microsofts_surface_laptop_ultra_with_nvidias_rtx_spark_is_coming_this_fall-news-73066.php", "snippet": "Microsoft's next Surface will be its most powerful yet. The Microsoft
Surface Laptop Ultra was just announced at Computex 2026, and it's taking the MacBook Pro head-on.\nThe Surface Laptop Ultra packs the just-announced [Nvidia RTX
Spark](https://www.gsmarena.com/nvidia_unveils_rtx_spark_computer_chip_with_up_to_20_cores_rtx_5070__128gb_ram-news-73061.php) system on a chip. It packages up to 20 ARM CPU cores, up to 128GB of
LPDDR5X unified RAM, and a Blackwell GPU with 6,144 CUDA cores, which Mic", "api_data": null, "hint": null}, {"title": "NVIDIA CEO Jensen Huang promises new 'RTX Spark' Windows on Arm chips will run
every Windows app ever made | Windows Central", "url": "https://www.windowscentral.com/hardware/laptops/nvidia-ceo-jensen-huang-promises-new-rtx-spark-windows-on-arm-chips-will-run-every-windows-app-
ever-made", "snippet": "For the quickest way to join, simply enter your email below and get access. We will send a confirmation and sign you up to our newsletter to keep you updated on all your gaming
news.\nJoin the club for quick access. Enter your email below and we'll send confirmation, and sign you up to our newsletter.\nBy submitting your information, you confirm you are aged 16 or
over,\nhave read our\nPrivacy Policy\nand agree to the\nTerms & Conditions. Geographical rules apply.\nIn an attempt to quell people's conce", "api_data": null, "hint": null}, {"title": "Nvidia N1X
officially confirmed to arrive as the RTX Spark - Notebookcheck News", "url": "https://www.notebookcheck.net/Nvidia-N1X-officially-confirmed-to-arrive-as-the-RTX-Spark.1312010.0.html", "snippet": "The
Nvidia RTX Spark has officially been shown off at Computex 2026\nNvidia\u2019s first consumer-grade laptop chip, the RTX Spark, is finally here. It is essentially a modified version of the DGX Spark
launched last year, but with Windows support.\nNvidia\u2019s long-awaited Windows on ARM chip is finally here. It is made on an unspecified 3 nm node from TSMC. Formerly known as the N1X, which was
likely its internal codename, the chip will launch as the RTX Spark. It won\u2019t be the only one, with Nvidia stat", "api_data": null, "hint": null}, {"title": "MSI unveils its first Nvidia RTX
Spark-powered laptop, the Prestige N16 Flip AI+", "url": "https://overclock3d.net/news/systems/msi-unveils-its-first-nvidia-rtx-spark-powered-laptop-the-prestige-n16-flip-ai/", "snippet": "MSI unveils
its first Nvidia RTX Spark-powered laptop, the Prestige N16 Flip AI+\nMSI partners with Nvidia to release one of the first RTX Spark Laptops\nAt Computex 2026, MSI has unveiled one of the world\u2019s
first Nvidia RTX Spark-powered laptops, the Prestige N16 Flip AI+. This premium thin-and-light laptop features Nvidia\u2019s new RTX Spark Superchip, which brings together a 20-core ARM processor and
Blackwell RTX graphics with up to 128GB of Unified memory.\nThe Prestige N16 Flip AI+ is a two-in-on", "api_data": null, "hint": null}, {"title": "Nvidia debuts RTX Spark processor for Windows
laptops, taking aim at Intel, AMD", "url": "https://finance.yahoo.com/news/nvidia-debuts-rtx-spark-processor-for-windows-laptops-taking-aim-at-intel-amd-053000567.html", "snippet": "Nvidia
([NVDA](https://finance.yahoo.com/quote/NVDA/)) is taking aim at Intel ([INTC](https://finance.yahoo.com/quote/INTC/)) and AMD ([AMD](https://finance.yahoo.com/quote/AMD/)) with the debut of its RTX
Spark superchip for Windows laptops. The processor, which includes a Blackwell GPU and Grace CPU, will power laptops from manufacturers including ASUS, Dell
([DELL](https://finance.yahoo.com/quote/DELL/)), HP ([HPQ](https://finance.yahoo.com/quote/HPQ/)), and Microsoft ([MSFT](https://finance.", "api_data": null, "hint": null}, {"title": "HP Debuts PCs
Built for the Next Wave of Windows PC Experiences Powered by NVIDIA RTX Spark\u2122", "url": "https://www.hp.com/us-en/newsroom/press-releases/2026/computex.html", "snippet": "Press Release\nHP Debuts
PCs Built for the Next Wave of Windows PC Experiences Powered by NVIDIA RTX Spark\u2122\nUnified portfolio delivers pre\u2011configured tools and secure local processing to accelerate AI workflows for
creators, developers, and gamers\nJune 1, 2026\nTAIPEI, June 1, 2026 \u2014 Today, HP Inc. (NYSE: HPQ) announced its latest devices and solutions, designed to enable developers of all types to create
new experiences using AI.\nHP is previewing PCs powered by NVIDIA RTX Spark\u2122, bringing a reinv", "api_data": null, "hint": null}, {"title": "NVIDIA RTX Spark Laptops: Specs, Models, Price,
Release Date, Benchmarks, and What We Know So Far - Kingy AI", "url": "https://kingy.ai/news/nvidia-rtx-spark-laptops-the-complete-guide-to-nvidias-bid-to-reinvent-the-windows-pc/", "snippet": "On May
31\u2013June 1, 2026, on a stage in Taipei during NVIDIA\u2019s GTC Taipei keynote at Computex 2026, Jensen Huang did something that would have sounded like science fiction just three years earlier.
He stood next to Microsoft\u2019s Satya Nadella and declared that \u201cthe PC is being reinvented,\u201d then introduced NVIDIA RTX Spark \u2014 a [Grace Blackwell
\u201csuperchip](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/)\u201d that drops a data-center-class AI architecture into thin Windows la", "api_data": null, "hint":
null}, {"title": "NVIDIA RTX Spark \u2014 Slim Laptops & Small Desktops", "url": "https://www.nvidia.com/en-us/products/rtx-spark/", "snippet": "RTX Spark Superchip\nUp to\nBlackwell RTX GPU\nUp
to\nUltra-Efficient CPU\nUp to\nFP4 AI Performance\nUp to\nUnified Memory\nCUDA, the software that accelerates the world\u2019s AI, runs natively on RTX Spark.\nThe most power-efficient RTX chip ever
made, in a chassis so slim you'll forget you\u2019re carrying it.\nMake a million ideas happen with hundreds of creative apps and AI tools supercharged by RTX and [NVIDIA
Studio](https://www.nvidia.com/en-us/studio/) tools.\nPlay the latest and greatest games with world-l", "api_data": null, "hint": null}, {"title": "Microsoft Announces Surface Laptop Ultra With Nvidia
RTX Spark Chip - Thurrott.com", "url": "https://www.thurrott.com/hardware/336854/microsoft-announces-surface-laptop-ultra-with-nvidia-rtx-spark-chip", "snippet": "![Microsoft Surface Laptop
Ultra](https://thurrott-assets.nyc3.digitaloceanspaces.com/web/wp-content/uploads/sites/2/2026/06/Microsoft-Surface-Laptop-Ultra.jpg)\nMicrosoft has just announced the Surface Laptop Ultra, which will
be powered by Nvidia\u2019s new RTX Spark chip for premium ARM-based laptops and mini PCs. The Surface Laptop Ultra will start shipping later this fall alongside other RTX Spark-powered devices, and
[Microsoft said](https://blogs.windows.com/devices/2026/05/31/introducing-surfa", "api_data": null, "hint": null}, {"title": "Nvidia ARM Laptop Chip N1X Confirmed for Computex: CUDA and RTX 5070 GPU
Onboard", "url": "https://www.techtimes.com/articles/317428/20260530/nvidia-arm-laptop-chip-n1x-confirmed-computex-cuda-rtx-5070-gpu-onboard.htm", "snippet": "![Dell
XPS](https://d.techtimes.com/en/full/465668/dell-xps.jpg?w=836&f=4e198fc4a2667e97596fceb391ab97a7)\nOn Friday morning, Nvidia, Microsoft, and Arm each posted the identical message to X \u2014 \"A new
era of PC\" \u2014 followed by the GPS coordinates of the Taipei Music Center, where [Nvidia CEO Jensen Huang is scheduled to deliver his GTC Taipei keynote on June 1](https://www.nvidia.com/en-
tw/gtc/taipei/computex/). One day later, VideoCardz reported that Dell has an embargoed XPS laptop launch powere", "api_data": null, "hint": null}, {"title": "NVIDIA N1 N1X laptop chips: Computex
reveal 1 June | tbreak", "url": "https://tbreak.com/nvidia-n1-n1x-laptop-chips-computex/", "snippet": "NVIDIA's long-rumoured N1 and N1X laptop chips are set for official announcement at Computex,
with CEO Jensen Huang delivering a keynote on 1 June 2026. As [reported by VideoCardz](https://videocardz.com/newz/nvidia-teases-new-era-of-pc-ahead-of-n1-and-n1x-laptop-chip-
announcement?ref=tbreak.com), multiple partners including ASUS and Microsoft are already teasing devices powered by these Arm-based processors that promise a \"new era of PC.\"\nKey Takeaways\n-
NVIDIA CEO Jensen Huang will announce N1", "api_data": null, "hint": null}, {"title": "NVIDIA N1x & N1 laptop chip specifications - VideoCardz.com", "url":
"https://videocardz.com/newz/nvidia-n1x-n1-laptop-chip-specifications", "snippet": "NVIDIA N1 specs\n![](https://cdn.videocardz.com/1/2026/05/NVIDIA-N1-JENSEN-HERO-1200x665.jpg)\nThis is what I call a
last-minute leak. One of our insiders provided preliminary specifications for the N1 series, confirming that the full N1X uses the same configuration as GB10 in DGX Spark. We have also learned about
three other N1 chip variants. The standard N1 is entirely new and perhaps more interesting, as it may target a more affordable segment.\nNVIDIA N1x\nThe N1X is listed with a 20 (10+10) CPU",
"api_data": null, "hint": null}, {"title": "Nvidia jumps into PCs with new Arm-based chip debuting in laptops from Microsoft, Dell, HP", "url": "https://www.cnbc.com/2026/05/31/nvidias-new-chip-to-
power-fresh-line-of-windows-laptops-by-dell-hp.html", "snippet": "[Nvidia](https://www.cnbc.com/quotes/NVDA/) has emerged as the world's most valuable company by dominating the market for artificial
intelligence chips in the data center. Now the company is expanding its prowess to chips that will serve as the main processor for personal computers, entering an arena that's long been ruled by
[Intel](https://www.cnbc.com/quotes/INTC/), [Advanced Micro Devices](https://www.cnbc.com/quotes/AMD/), [Qualcomm](https://www.cnbc.com/quotes/QCOM/) and [Apple](https://ww", "api_data": null, "hint":
null}, {"title": "ASUS just dropped the ultimate Arm-based creator laptops; 128GB of RAM and NVIDIA Blackwell in a 13mm chassis.", "url": "https://www.windowscentral.com/hardware/asus/asus-
proart-p16-and-p14-n1x-computex-2026", "snippet": "For the quickest way to join, simply enter your email below and get access. We will send a confirmation and sign you up to our newsletter to keep you
updated on all your gaming news.\nJoin the club for quick access. Enter your email below and we'll send confirmation, and sign you up to our newsletter.\nBy submitting your information, you confirm
you are aged 16 or over,\nhave read our\nPrivacy Policy\nand agree to the\nTerms & Conditions. Geographical rules apply.\nI have been saying for months that Wi", "api_data": null, "hint": null},
{"title": "Computex 2026 Will Be NVIDIA's Biggest Event Of The Year. Here's What To Expect", "url": "https://wccftech.com/nvidia-computex-2026-what-to-expect/", "snippet": "Although CES 2026 was a
massive disappointment for consumers, Computex 2026 looks to inject some much-needed excitement back into the beleaguered tech space.\nIn what is arguably the biggest consumer hardware launch of the
year, [Nvidia ](https://x.com/nvidia/status/2060390710797328574)and [ARM ](https://x.com/Arm/status/2060483398746214837)have already started teasing their highly anticipated N1X laptop chip, an APU
based on the same [GB10 chip ](https://wccftech.com/nvidia-gb10-superchip-soc-3n", "api_data": null, "hint": null}, {"title": "Surface Laptop Ultra: Microsoft and NVIDIA reveal the 128GB RAM,
mini\u2011LED, RTX Spark powerhouse redefining Windows on Arm | Windows Central", "url": "https://www.windowscentral.com/hardware/surface/microsoft-surface-laptop-ultra-announced-computex-2026",
"snippet": "For the quickest way to join, simply enter your email below and get access. We will send a confirmation and sign you up to our newsletter to keep you updated on all your gaming news.\nJoin
the club for quick access. Enter your email below and we'll send confirmation, and sign you up to our newsletter.\nBy submitting your information, you confirm you are aged 16 or over,\nhave read
our\nPrivacy Policy\nand agree to the\nTerms & Conditions. Geographical rules apply.\nFor months, I have been teasing on th", "api_data": null, "hint": null}, {"title": "NVIDIA N1X Preview: The First
Blackwell Laptop Chip and What It Means for Local AI \u2014 ChatForest", "url": "https://chatforest.com/reviews/nvidia-n1x-computex-2026-blackwell-laptop-ai-pc-preview/", "snippet": "Jensen Huang
takes the Computex stage on June 1, 2026 at GTC Taipei \u2014 and for the first time, an NVIDIA chip is expected to live inside a laptop rather than a data center rack. The N1X is an ARM-based SoC co-
developed with MediaTek, packing a Blackwell-architecture GPU with 6,144 CUDA cores alongside a 20-core ARM CPU. This is a preview based on pre-announcement leaks and confirmed specifications.\nWhat
Is the N1X?\nThe N1X is NVIDIA\u2019s first laptop system-on-chip \u2014 a single die combining CPU and G", "api_data": null, "hint": null}, {"title": "New PC era: Lenovo laptop leak unveils first
Nvidia N1X notebooks and high prices - Notebookcheck News", "url": "https://www.notebookcheck.net/New-PC-era-Lenovo-laptop-leak-unveils-first-Nvidia-N1X-notebooks-and-high-prices.1311489.0.html",
"snippet": "A retailer leak reveals a 15.3-inch Lenovo Yoga Pro 7 based on Nvidia N1X with fairly high prices\nThe new PC era announced by Nvidia might be starting with Lenovo. A new retailer leak
just a few hours before the official launch event reveals not only a new Lenovo Yoga Pro 7 laptop based on Nvidia's ARM APU, but also three planned model variants and prices. The latter do not
necessarily point to a price war with the Snapdragon X2 Elite.\nThe Yoga Pro 7 has previously been available with an Intel c", "api_data": null, "hint": null}, {"title": "Microsoft x NVIDIA \u201cNew
Era of PC\u201d Tease: Arm N1X Rumor Heads to Computex | Windows Forum", "url": "https://windowsforum.com/threads/microsoft-x-nvidia-new-era-of-pc-tease-arm-n1x-rumor-heads-to-computex.420821/",
"snippet": "Microsoft and NVIDIA jointly teased \u201ca new era of PC\u201d on May 29, 2026, using matching social posts that point toward Computex in Taipei and have intensified speculation that
NVIDIA\u2019s long-rumored Arm-based N1X PC chip may finally be unveiled next week. The companies have not confirmed the product, and Microsoft\u2019s Windows and Surface chief has already said the
tease is not about a new Windows version. But the choreography matters: when the Windows platform owner and the dominant GPU vendor use th", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Computex announcement to retail availability timeline laptop chip new platform weeks months"
}
```

### 📋 Result

```
{"query": "Computex announcement to retail availability timeline laptop chip new platform weeks months", "results": [{"title": "Microsoft Introduces Surface Laptop Ultra with NVIDIA RTX Spark at
Computex 2026 | Technobezz", "url": "https://www.technobezz.com/news/microsoft-introduces-surface-laptop-ultra-with-nvidia-rtx-spark-at-computex-2026", "snippet": "[Microsoft just announced the
Surface Laptop Ultra](https://blogs.windows.com/devices/2026/05/31/introducing-surface-laptop-ultra-made-for-world-makers/) at Computex 2026, and it kills the old playbook. This is not a thin-and-
light for email.\nIt is a 1-petaflop AI workstation in a sub-18 mm chassis, [co-engineered with NVIDIA](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark) around the
newly announced RTX Spark chip. The [RTX Spark silicon pairs a Blackwell RTX G", "api_data": null, "hint": null}, {"title": "Nvidia unveils RTX Spark Superchip for laptops and desktop PCs at Computex
2026 \u2013 new platform promises to turn Windows into an agentic AI OS with Arm CPU, Blackwell GPU, and 128GB unified memory | Tom's Hardware", "url": "https://www.tomshardware.com/laptops/nvidia-
unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory", "snippet": "Nvidia unveils RTX Spark
Superchip for laptops and desktop PCs at Computex 2026 \u2013 new platform promises to turn Windows into an agentic AI OS with Arm CPU, Blackwell GPU, and 128GB unified memory\nNvidia is transforming
Windows into an agentic AI platform at Computex 2026. During his keynote, CEO Jensen Huang revealed the RTX Spark: a Windows on Arm platform for laptops powered by the company's RTX Spark Superchip.
The company boldly claims that this platform is \u201cthe most efficient ever built,\u201d a", "api_data": null, "hint": null}, {"title": "Nvidia ARM Laptop Chip N1X Confirmed for Computex: CUDA and
RTX 5070 GPU Onboard", "url": "https://www.techtimes.com/articles/317428/20260530/nvidia-arm-laptop-chip-n1x-confirmed-computex-cuda-rtx-5070-gpu-onboard.htm", "snippet": "![Dell
XPS](https://d.techtimes.com/en/full/465668/dell-xps.jpg?w=836&f=4e198fc4a2667e97596fceb391ab97a7)\nOn Friday morning, Nvidia, Microsoft, and Arm each posted the identical message to X \u2014 \"A new
era of PC\" \u2014 followed by the GPS coordinates of the Taipei Music Center, where [Nvidia CEO Jensen Huang is scheduled to deliver his GTC Taipei keynote on June 1](https://www.nvidia.com/en-
tw/gtc/taipei/computex/). One day later, VideoCardz reported that Dell has an embargoed XPS laptop launch powere", "api_data": null, "hint": null}, {"title": "Intel Arc G3 Arrives Before Computex:
First Dedicated Handheld Chip Challenges AMD Ryzen Z2", "url": "https://www.techtimes.com/articles/317331/20260528/intel-arc-g3-arrives-before-computex-first-dedicated-handheld-chip-challenges-amd-
ryzen-z2.htm", "snippet": "![Intel ARC Chip](https://d.techtimes.com/en/full/465566/intel-arc-chip.png?w=836&f=5c37c26faa84588a24777c38c448cd89)\nIntel unveiled the [Arc G3 and Arc G3
Extreme](https://www.eteknix.com/intel-arc-g3-could-be-officially-announced-on-may-28-for-gaming-handhelds/) on May 28, 2026 \u2014 the company's first chips designed exclusively for gaming handhelds
rather than adapted from existing laptop lines. The announcement arrived five days before Computex 2026 opens in Taipei, giving Intel's OEM partners ", "api_data": null, "hint": null}, {"title":
"Nvidia Announces RTX Spark Processor Family for Laptops and Desktops at Computex 2026 | Technobezz", "url": "https://www.technobezz.com/news/nvidia-announces-rtx-spark-processor-family-for-laptops-
and-desktops-at-computex-2026", "snippet": "Nvidia declared itself a PC chipmaker on Monday, [announcing the RTX Spark processor family at Computex 2026](https://nvidianews.nvidia.com/news/nvidia-
microsoft-windows-pcs-agents-rtx-spark) in Taipei and kicking off what CEO Jensen Huang called \"the first completely reengineered, reinvented line of PCs that has happened in 40 years.\" The RTX
Spark combines a [20-core Arm-based Grace CPU](https://arstechnica.com/gadgets/2026/06/nvidia-gets-into-the-arm-pc-business-with-new-high-end-rtx-spark-pr", "api_data": null, "hint": null}, {"title":
"Computex 2026 Live: Every update and announcement from day one in Taipei | Tom's Hardware", "url": "https://www.tomshardware.com/news/live/computex-2026-", "snippet": "Computex 2026 Live: Every
update and announcement from day one in Taipei\nWe're boots on the ground in Taiwan\n[News](https://www.tomshardware.com/news)\n[Stephen Warwick](https://www.tomshardware.com/author/stephen-
warwick)Contributions from\n[Jeffrey Kampman](https://www.tomshardware.com/author/jeffrey-kampman),\n[Paul Alcorn](https://www.tomshardware.com/author/paul-alcorn),\n[Joe
Shields](https://www.tomshardware.com/author/joe-shields),\n[Jake Roach](https://www.tomshardware.com/author/jake-roach)", "api_data": null, "hint": null}, {"title": "Computex 2026 Will Be
NVIDIA\u2019s Biggest Event Of The Year. Here\u2019s What To Expect", "url": "https://wccftech.com/nvidia-computex-2026-what-to-expect/", "snippet": "Although CES 2026 was a massive disappointment for
consumers, Computex 2026 looks to inject some much-needed excitement back into the beleaguered tech space.\nIn what is arguably the biggest consumer hardware launch of the year, [Nvidia
](https://x.com/nvidia/status/2060390710797328574)and [ARM ](https://x.com/Arm/status/2060483398746214837)have already started teasing their highly anticipated N1X laptop chip, an APU based on the
same [GB10 chip ](https://wccftech.com/nvidia-gb10-superchip-soc-3n", "api_data": null, "hint": null}, {"title": "Live Updates From Computex 2026 \ud83d\udd34", "url": "https://gizmodo.com/live-
updates-from-computex-2026-2000761697", "snippet": "Computex 2026 is set to be the most consequential computing conference in many years.\nThe [annual computing
showcase](https://www.computextaipei.com.tw/en/index.html) set to take over Taipei, Taiwan, from June 2 through June 5 will bring us all-new computing platforms we\u2019ve been hinted at for months.
While Nvidia gets busy hyping its own new ARM-based CPUs, we\u2019ll likely see refreshed laptops hoping to fight back against the budget-end king of the ring, the [MacBook
Neo](https://gizmodo.com/macbo", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Now I have a clear picture. Let me analyze the situation:

**Key Facts:**
1. Nvidia officially unveiled RTX Spark (the consumer branding for N1/N1X) at Computex 2026 on June 1, 2026
2. All OEMs say "Fall 2026" availability - no specific dates
3. NO pre-orders are available from any OEM as of June 2, 2026
4. No official pricing has been announced
5. No benchmarks have been shared
6. The question asks if any N1/N1X PC will be available for consumer purchase by June 13, 2026


7. With only a ~12-day window between announcement and the deadline, and historical precedent showing 2+ months typically elapse before retail availability, it's virtually certain no consumer units will be purchasable by June 13th. The timeline for RTX Spark availability by July 31 is essentially impossible—we're talking about a brand-new platform with no pricing, no pre-orders, and an official "Fall 2026" target, all within roughly two weeks of announcement. Even considering edge cases like region-locked launches or Chinese retailer listings, the lack of any concrete availability signals puts this at around 2-3% probability at best.

Though I should double-check that Notebookcheck leak about the Lenovo Yoga Pro 7 to see if there's something I'm missing there.

## 💬 Response

Let me check the Lenovo pricing leak more carefully:

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.notebookcheck.net/New-PC-era-Lenovo-laptop-leak-unveils-first-Nvidia-N1X-notebooks-and-high-prices.1311489.0.html",
  "prompt": "What are the specific prices, models, and availability dates mentioned for the Lenovo RTX Spark / N1X laptops? Is there any mention of pre-order or on-sale dates?"
}
```

### 📋 Result

```
{"url": "https://www.notebookcheck.net/New-PC-era-Lenovo-laptop-leak-unveils-first-Nvidia-N1X-notebooks-and-high-prices.1311489.0.html", "content": "Based on the content:\n\n**Prices and Models:**\n-
**Lenovo Yoga Pro 7 15.3-inch** with Nvidia N1X 675 + 64GB RAM: \u20ac4,049\n- **Lenovo Yoga Pro 7 15.3-inch** with Nvidia N1X 650 + 32GB RAM: \u20ac3,199\n- A third variant with **Nvidia N1 chip** is
mentioned but no price is provided\n\nAll models feature a 165Hz WQXGA OLED touchscreen, 1TB PCIe SSD, and Windows 11 Home.\n\n**Availability Dates:**\n- The article states the leak came \"just a few
hours before the official launch event\"\n- Launch event date: **June 1, 2026** (Computex opening by Nvidia CEO Jensen Huang)\n- Launches expected \"next week\" from various manufacturers\n\n**Pre-
order/On-sale Dates:**\nNo specific pre-order or on-sale dates are mentioned in the content.\n\n**Note:** The article refers to these as \"retailer leaks\" from Eastern Europe, so these are not
official announcements.\n\nRelevant links:\nNo specific product or source links are included in the provided text content.", "title": "New PC era: Lenovo laptop leak unveils first Nvidia N1X notebooks
and high prices"}
```

```json
{
  "query": "\"RTX Spark\" OR \"N1X\" pre-order date \"June\" OR \"July\" 2026 available shipping"
}
```

### 📋 Result

```
{"query": "\"RTX Spark\" OR \"N1X\" pre-order date \"June\" OR \"July\" 2026 available shipping", "results": [{"title": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs at Computex 2026
\u2014 three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman | Tom's Hardware", "url": "https://www.tomshardware.com/pc-components/cpus/nvidia-unveils-dgx-sparrk-roadmap-for-
laptops-and-desktop-pcs-at-computex-2026-three-generations-outlined-rubin-followed-by-rosa-feynman", "snippet": "Nvidia lays out RTX Spark roadmap for laptops and desktop PCs at Computex 2026 \u2014
three generations outlined, Rubin with LPDDR6 memory, followed by Rosa Feynman\nAlong with its first-generation RTX Spark platform for desktop and laptop PCs, Nvidia CEO Jensen Huang revealed the
company's commitment to future generations of those platforms on its future roadmaps. The company is committed to producing at least two additional generations of Spark platforms for its
partners.\nBeyond the Grace Blackwell ", "api_data": null, "hint": null}, {"title": "Nvidia N1X officially confirmed to arrive as the RTX Spark - Notebookcheck News", "url":
"https://www.notebookcheck.net/Nvidia-N1X-officially-confirmed-to-arrive-as-the-RTX-Spark.1312010.0.html", "snippet": "The Nvidia RTX Spark has officially been shown off at Computex
2026\nNvidia\u2019s first consumer-grade laptop chip, the RTX Spark, is finally here. It is essentially a modified version of the DGX Spark launched last year, but with Windows support.\nNvidia\u2019s
long-awaited Windows on ARM chip is finally here. It is made on an unspecified 3 nm node from TSMC. Formerly known as the N1X, which was likely its internal codename, the chip will launch as the RTX
Spark. It won\u2019t be the only one, with Nvidia stat", "api_data": null, "hint": null}, {"title": "NVIDIA and Microsoft Reinvent Windows PCs for the Age of Personal AI | NVIDIA Newsroom", "url":
"https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark", "snippet": "News Summary:\n- NVIDIA RTX Spark powers the world\u2019s first Windows PCs purpose-built for personal
agents, featuring 1 petaflop of AI performance, industry-leading power efficiency, full-stack NVIDIA AI and graphics technology, and up to 128GB of unified memory.\n- NVIDIA and Microsoft collaborate
to deliver a native Windows experience for personal agents, including new security primitives and NVIDIA OpenShell to run agents securely on primary devices.\n- RTX Spark lets creators, AI developers
and g", "api_data": null, "hint": null}, {"title": "Nvidia's N1X Apple Silicon rival is two years behind", "url": "https://appleinsider.com/articles/26/06/01/nvidias-n1x-apple-silicon-rival-is-two-
years-behind", "snippet": "Nvidia has stepped into the processor market with its RTX Spark, but at first glance, it's clearly behind [Apple Silicon](https://appleinsider.com/inside/apple-silicon) by a
considerable margin.\nComputex 2026 is underway, and Nvidia has [formally stepped](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/) into the processor ring with its own chip.
Nvidia calls the RTX Spark a \"superchip\" for Windows PCs that have massive AI performance.\nThis chip consists of an ARM-based Nvidia", "api_data": null, "hint": null}, {"title": "Watch out, Apple -
Nvidia just unveiled its RTX Spark Arm 'superchip' to take on the M5 at Computex 2026 | TechRadar", "url": "https://www.techradar.com/computing/computing-components/watch-out-apple-nvidia-just-
unveiled-its-rtx-spark-arm-superchip-to-take-on-the-m5-at-computex-2026", "snippet": "Sign up with your email below to instantly access member features, newsletters and exclusive Insider perks\nBy
submitting your information, you confirm you are aged 16 or over,\nhave read our\nPrivacy Policy\nand agree to the\nTerms & Conditions. Geographical rules apply.\nNvidia has just announced its new
Arm-based laptop chip at Computex 2026, firing a warning shot across the bow of Apple (who has found great success with its own Arm-based M-series chips), as well as Intel and AMD.\nWhile Nvidia has
", "api_data": null, "hint": null}, {"title": "Nvidia unveils RTX Spark Superchip for laptops and desktop PCs at Computex 2026 \u2013 new platform promises to turn Windows into an agentic AI OS with
Arm CPU, Blackwell GPU, and 128GB unified memory | Tom's Hardware", "url": "https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-
windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory", "snippet": "Nvidia unveils RTX Spark Superchip for laptops and desktop PCs at Computex 2026 \u2013 new platform
promises to turn Windows into an agentic AI OS with Arm CPU, Blackwell GPU, and 128GB unified memory\nNvidia is transforming Windows into an agentic AI platform at Computex 2026. During his keynote,
CEO Jensen Huang revealed the RTX Spark: a Windows on Arm platform for laptops powered by the company's RTX Spark Superchip. The company boldly claims that this platform is \u201cthe most efficient
ever built,\u201d a", "api_data": null, "hint": null}, {"title": "NVIDIA RTX Spark Specs, Release Date, and Everything You Need to Know", "url": "https://www.gizmochina.com/2026/06/01/nvidia-rtx-
spark-launch-specs-windows-on-arm-pc/", "snippet": "At Computex Taipei 2026, [NVIDIA](https://www.gizmochina.com/tag/nvidia/)\u2018s CEO took the stage and officially unveiled the RTX Spark, the
company\u2019s first-ever processor built specifically for Windows PCs. It\u2019s an Arm-based chip that packs a 20-core Grace CPU (built alongside MediaTek), a Blackwell RTX GPU with 6,144 CUDA
cores, an NPU, and up to 128GB of unified LPDDR5X memory, all on a single TSMC 3nm package.\nAs a result, NVIDIA says the RTX Spark is capable of 1 petaFLOP of AI performance. Th", "api_data": null,
"hint": null}, {"title": "NVIDIA \"N1 / N1X\" Comprehensive Summary \u2014 Is the Era of \"Carrying\" DGX Spark Finally Here?\uff5czephel01", "url": "https://note.com/zephel01/n/n6b736a19936c?hl=en-
US", "snippet": "![\u898b\u51fa\u3057\u753b\u50cf](https://assets.st-note.com/production/uploads/images/281327633/rectangle_large_type_2_3b6e0c06723b0a2b0b3d238197cdd3ff.png?width=1280)\nNVIDIA \"N1 /
N1X\" Comprehensive Summary \u2014 Is the Era of \"Carrying\" DGX Spark Finally Here?\nSummary of leaks and pre-release information as of May 31, 2026\n\u26a0\ufe0f This article is based on leaks and
observations prior to the official announcement. Figures and specifications are not finalized and may change at the NVIDIA keynote on June 1st. Please treat this a", "api_data": null, "hint": null},
{"title": "Nvidia Targets PC Market with N1X and RTX Spark | Let's Data Science", "url": "https://letsdatascience.com/news/nvidia-targets-pc-market-with-n1x-and-rtx-spark-4c665f04", "snippet": "Nvidia
Targets PC Market with N1X and RTX Spark\n![Nvidia Targets PC Market with N1X and RTX Spark](https://static.seekingalpha.com/cdn/s3/uploads/getty_images/1141488976/image_1141488976.jpg?io=getty-
c-w630)\n[\u00b7 rights & takedowns](https://letsdatascience.com/copyright)\nDuring a Computex keynote, Nvidia CEO Jensen Huang unveiled an Arm-based CPU called N1X and an integrated superchip family
named RTX Spark, which CNBC reports will debut this fall in Windows laptops from Microsoft, Dell, HP, ASUS,", "api_data": null, "hint": null}, {"title": "[News] NVIDIA Enters PC Market with RTX Spark
Featuring MediaTek-Co-Designed N1X CPU on TSMC 3nm", "url": "https://www.trendforce.com/news/2026/06/01/news-nvidia-enters-pc-market-with-rtx-spark-featuring-mediatek-co-designed-n1x-cpu-on-
tsmc-3nm/", "snippet": "[News] NVIDIA Enters PC Market with RTX Spark Featuring MediaTek-Co-Designed N1X CPU on TSMC 3nm\n![](https://img.trendforce.com/blog/wp-
content/uploads/2026/06/01150725/nvidia-rtx-spark-624x351.png)\nAs traditional CPU leaders such as Intel push further into the AI accelerator market, NVIDIA is moving in the opposite
direction\u2014leveraging its dominance in AI computing to expand into the PC processor arena. At GTC Taipei on June 1, CEO Jensen Huang unveiled the NVIDIA RTX Spark, developed in partne",
"api_data": null, "hint": null}]}
```

## 💭 Thinking

Now I have a very clear picture. Let me synthesize my analysis:

**Key facts:**
1. RTX Spark (formerly N1/N1X) was officially unveiled at Computex on June 1, 2026 - just yesterday
2. ALL sources consistently say "Fall 2026" availability
3. No pre-orders available from any OEM
4. No official pricing announced
5. No benchmarks shared yet
6. The Lenovo leak showed prices in Eastern European retailers but NO availability dates
7. The question window is June 1-13, 2026 - only ~12 days after announcement

**Historical precedent for new platform launches:**


New architectures like ARM for Windows typically need months between announcement and retail availability. Even Snapdragon X Elite, which had months of pre-announcement buildup and committed ship dates before Computex 2024, didn't see retail laptops until about two weeks after the event. RTX Spark has none of that groundwork—no committed timelines, no pricing, no pre-orders open anywhere.

For a YES answer to happen in the next 12 days, we'd need something unprecedented: either an immediate same-week retail launch or pre-orders opening with actual payment processing and binding commitments.

Against it, every public statement points to Fall 2026, there's no pricing or pre-order infrastructure, the platform is brand new and needs validation, LPDDR5X supply is constrained, Windows on ARM software readiness was already cited as a delay factor, and no OEM has committed to anything more specific than "Fall." Even benchmarks haven't been released yet. The only weak signal is that Lenovo Yoga Pro 7 leak showing up in an Eastern European retailer database with prices, which hints some systems might be further along than publicly stated, and Chinese retailers sometimes get early access. But even that leak didn't include availability dates—just pricing.

This kind of database activity is typical months before actual retail launch. Given the official timeline is still "Fall 2026" (3-5 months out), no pricing, no pre-orders, and no benchmarks, I'm setting my confidence at 3%.

## 💬 Response

Now I have a comprehensive picture. Let me run my reflection and premortem.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Official Nvidia/OEM timeline is 'Fall 2026' - all sources consistently say this, meaning September-November 2026 at earliest",
      "logit": -3,
      "confidence": 0.95
    },
    {
      "description": "No pre-orders available from any OEM as of June 2, 2026; no pricing announced; no benchmarks shared - the product pipeline is months from retail",
      "logit": -2.5,
      "confidence": 0.95
    },
    {
      "description": "Brand new silicon platform (first Nvidia ARM consumer chip + Windows on ARM) historically requires months of validation, driver maturation, and OEM QA before retail",
      "logit": -2,
      "confidence": 0.85
    },
    {
      "description": "The original launch was delayed from Q3 2025 to 2026 due to Windows on ARM readiness, memory supply issues, and silicon revisions - suggesting the ecosystem is not mature enough for immediate retail",
      "logit": -1,
      "confidence": 0.7
    },
    {
      "description": "Lenovo Yoga Pro 7 appeared in Eastern European retailer database with prices, suggesting some OEMs may be further along in preparation than publicly acknowledged",
      "logit": 0.3,
      "confidence": 0.3
    },
    {
      "description": "Pre-orders with binding payment and ship date before July 31 would count - theoretically an OEM could open pre-orders during Computex week",
      "logit": 0.2,
      "confidence": 0.15
    },
    {
      "description": "Chinese market (JD.com) sometimes gets early product listings - the N1 motherboard was already spotted on Goofish at $1,400",
      "logit": 0.2,
      "confidence": 0.15
    }
  ],
  "tentative_estimate": {
    "logit": -3.5,
    "probability": 0.03
  },
  "anchor": "Historical base rate for brand-new silicon platform going from Computex announcement to consumer retail availability within 2 weeks: essentially 0%. Even Snapdragon X Elite (Computex 2024) had committed ship dates months in advance. No precedent for an entirely new platform architecture shipping within 2 weeks of initial unveil with no pre-announced pricing or availability dates. Base rate ~2%.",
  "assessment": "This question asks whether any N1/N1X (now branded RTX Spark) Windows PC will be available for consumer purchase within ~12 days of the Computex announcement. The evidence overwhelmingly points to NO:\n\n1. EVERY source - Nvidia, Microsoft, all OEMs, all tech press - consistently says 'Fall 2026' availability\n2. No pricing has been announced by any OEM\n3. No pre-orders are available or announced\n4. No benchmarks have been shared (suggesting products are far from retail readiness)\n5. This is an entirely new platform architecture (ARM for Windows from Nvidia) requiring extensive ecosystem validation\n6. The original launch was already delayed ~1 year due to readiness issues\n\nThe only conceivable YES path would be:\n- A surprise pre-order opening with binding payment and ship date \u2264July 31, 2026\n- An unauthorized Chinese retailer listing\n\nBoth are extremely unlikely given the complete absence of pricing, the consistent 'Fall 2026' messaging, and the fact that even benchmarks haven't been shared yet. The question's own description notes 'the typical gap between a Computex unveil and retail availability of a brand-new silicon platform is measured in months, not weeks.'",
  "calibration_notes": "My 3% estimate is near the floor for binary questions. The 3% accounts for unknown unknowns: a surprise pre-order, an unauthorized early listing, or a Chinese market play. But the structural barriers (no pricing, no pre-orders, no benchmarks, 'Fall 2026' timeline) make even these scenarios very unlikely within 12 days.",
  "key_uncertainties": "The main uncertainty is whether any OEM might open pre-orders (with binding payment and ship date \u2264 July 31) during Computex week as a surprise. This is the only realistic YES path, but there's zero evidence suggesting this will happen.",
  "update_triggers": "- Any OEM opens pre-orders with binding payment and stated ship date \u2264 July 31 \u2192 would move to ~80%+\n- A retailer (especially JD.com or Amazon) lists an RTX Spark laptop with 'Add to Cart' and stated availability \u2192 would resolve YES\n- Nvidia or Microsoft announces immediate availability of any SKU \u2192 would resolve YES",
  "tool_audit": "research() returned comprehensive findings from Tom's Hardware, The Verge, Nvidia official sources, and others. web_search() confirmed Fall 2026 timeline consistently across all sources. fetch_url() on Notebookcheck confirmed Lenovo leak had prices but NO availability dates. All tools worked well and returned consistent information.",
  "process_reflection": "This was a straightforward question to research - the evidence is overwhelmingly one-directional. The research() tool provided excellent comprehensive coverage. The main challenge was ensuring I didn't miss any surprise availability announcement, which web_search() helped confirm doesn't exist."
}
```

### 📋 Result

```
{"factor_count": 7, "factor_sum": -7.475, "tentative_logit": -3.5, "logit_gap": 3.9749999999999996, "neutral_factor_count": 0, "factor_breakdown": [{"description": "Official Nvidia/OEM timeline is
'Fall 2026' - all sources consistently say this, meaning September-November 2026 at earliest", "logit": -3.0, "confidence": 0.95, "effective_logit": -2.8499999999999996}, {"description": "No pre-
orders available from any OEM as of June 2, 2026; no pricing announced; no benchmarks shared - the product pipeline is months from retail", "logit": -2.5, "confidence": 0.95, "effective_logit":
-2.375}, {"description": "Brand new silicon platform (first Nvidia ARM consumer chip + Windows on ARM) historically requires months of validation, driver maturation, and OEM QA before retail",
"logit": -2.0, "confidence": 0.85, "effective_logit": -1.7}, {"description": "The original launch was delayed from Q3 2025 to 2026 due to Windows on ARM readiness, memory supply issues, and silicon
revisions - suggesting the ecosystem is not mature enough for immediate retail", "logit": -1.0, "confidence": 0.7, "effective_logit": -0.7}, {"description": "Lenovo Yoga Pro 7 appeared in Eastern
European retailer database with prices, suggesting some OEMs may be further along in preparation than publicly acknowledged", "logit": 0.3, "confidence": 0.3, "effective_logit": 0.09}, {"description":
"Pre-orders with binding payment and ship date before July 31 would count - theoretically an OEM could open pre-orders during Computex week", "logit": 0.2, "confidence": 0.15, "effective_logit":
0.03}, {"description": "Chinese market (JD.com) sometimes gets early product listings - the N1 motherboard was already spotted on Goofish at $1,400", "logit": 0.2, "confidence": 0.15,
"effective_logit": 0.03}], "dominant_factor": "Official Nvidia/OEM timeline is 'Fall 2026' - all sources consistently say this, meaning September-November 2026 at earliest",
"dominant_effective_logit": -2.8499999999999996, "factor_implied_probability": 0.0005667643636340825, "tentative_probability": 0.03, "gap_pp": 2.9433235636365915, "sources": ["[(Metaculus) Will any
Nvidia N1- or N1X-powered Windows PC be available for purchase by consumers before June 14, 2026?](https://www.metaculus.com/questions/43745)", "[New PC era: Lenovo laptop leak unveils first Nvidia
N1X notebooks and high prices](https://www.notebookcheck.net/New-PC-era-Lenovo-laptop-leak-unveils-first-Nvidia-N1X-notebooks-and-high-prices.1311489.0.html)"]}
```

## 💬 Response

The reflection shows my factors imply an even lower probability (0.06%) than my tentative 3%. The gap is because my factors are individually very strong evidence, but I'm maintaining 3% as a floor to account for unknown unknowns. Now let me run the premortem.

## 🔧 Tool: mcp__premortem__premortem


```json
{
  "counterargument": "The strongest case for YES: The Lenovo Yoga Pro 7 already appeared in an Eastern European retailer database with specific prices (\u20ac3,199 and \u20ac4,049), which suggests OEM preparation is much further along than public messaging indicates. Companies sometimes use \"Fall 2026\" as a conservative public timeline while planning surprise early availability. Apple has done same-day keynote-to-availability launches. The Goofish listing of the N1 motherboard at $1,400 suggests finished hardware exists. Microsoft's Build conference on June 2 could feature a \"available today\" moment for Surface Laptop Ultra, similar to how Surface products have occasionally launched at announcement events. The question only requires ONE device in ONE country with binding pre-orders shipping by July 31 \u2014 a lower bar than full retail availability. If even one Chinese retailer on JD.com accepts binding orders with a July ship date, that would count.",
  "what_would_change_my_mind": "1. Any OEM (especially Microsoft or Lenovo) announces pre-orders opening within the next 12 days with a stated ship date \u2264 July 31, 2026 \u2014 this would move me to 70%+\n2. A major retailer (JD.com, Amazon, Best Buy) lists an RTX Spark device with a working \"Add to Cart\" button and stated availability \u2014 would move to 90%+\n3. A credible tech journalist reports seeing \"buy now\" or \"pre-order\" buttons on any RTX Spark laptop page \u2014 would move to 85%+\n4. Microsoft announces Surface Laptop Ultra with immediate pre-order availability at Build on June 2 \u2014 would move to 90%+",
  "confidence_in_estimate": 0.88
}
```

### 📋 Result

```
{"verdict": "approve", "assessment": "I verified all 7 factors against the research trace and found no errors.\n\n**Factor-by-factor verification:**\n1. \"Fall 2026\" timeline \u2014 confirmed by
Tom's Hardware, The Verge, Nvidia blog, CNBC, HP press release in the trace.\n2. No pre-orders/pricing/benchmarks \u2014 explicitly confirmed in research results: \"Pre-orders: NOT yet available,\"
\"No official prices announced,\" \"zero performance benchmarks.\"\n3. New silicon platform validation time \u2014 reasonable general inference, supported by Snapdragon X Elite comparison in
trace.\n4. Delay from Q3 2025 \u2014 trace confirms: \"Originally expected late 2025, pushed to 2026 due to Windows 11 26H1 OS timing, notebook demand, LPDDR5X memory supply.\"\n5. Lenovo Yoga Pro 7
retailer leak \u2014 confirmed via Notebookcheck fetch_url: \u20ac4,049 and \u20ac3,199 prices, but \"No specific pre-order or on-sale dates.\"\n6. Theoretical pre-order possibility \u2014 properly
flagged as speculative with 0.15 confidence.\n7. Goofish N1 motherboard \u2014 confirmed in trace: \"April 9, 2026: N1/N1X laptop motherboard with 128GB LPDDR5X surfaced on Goofish for $1,400.\" Minor
imprecision in conflating Goofish with JD.com in the factor description, but the core claim is grounded.\n\n**No double-counting:** Factors 1-4 each address distinct evidence (official timeline,
absence of readiness signals, general platform precedent, specific delay history).\n\n**No wrong-direction factors:** All negative logits correspond to evidence against availability; all positive
logits correspond to weak evidence for potential early availability.\n\n**No contradictory assessment:** The \"overwhelmingly NO\" narrative matches the factor balance (net logit strongly
negative).\n\n**Resolution criteria properly recovered:** Agent fetched the Metaculus question page and engaged with specific criteria (pre-orders with binding payment, ship date \u2264 July 31,
region-locked launches counting).\n\n**Counterargument quality:** Substantive \u2014 raises Apple same-day launches, Microsoft Build surprise, Lenovo leak suggesting advanced preparation, JD.com
scenario. Not a token gesture.\n\n**Probability assessment:** 3% is well-calibrated. My independent estimate based on the evidence would be 2-4%. The mathematical factor combination suggests 0.06%,
and the agent reasonably applied a floor for tail risk from unknown unknowns. The 1pp departure from the 2% anchor is minimal and justified.\n\n**Confidence:** 0.88 is appropriate given the strong,
consistent evidence with modest uncertainty about the forward 12-day window.\n\n**Tool audit:** Agent's narrative matches actual metrics (9 calls, 0 errors). No discrepancies."}
```

## 💬 Response

The premortem approved. Now let me submit my final forecast.

## 🔧 Tool: StructuredOutput


```json
{
  "anchor": "Historical base rate for a brand-new silicon platform (new architecture, new vendor in the space) going from Computex/trade show announcement to consumer retail availability within 2 weeks, with no pre-announced pricing or ship dates: ~2-3%. Even the Snapdragon X Elite launch (Computex 2024) had committed ship dates months in advance. No precedent exists for immediate retail of a completely new platform architecture.",
  "anchor_logit": -3.5,
  "factors": [
    {
      "description": "Official Nvidia/OEM timeline is 'Fall 2026' \u2014 every source (Nvidia, Microsoft, Dell, Lenovo, HP, ASUS, MSI, Tom's Hardware, The Verge, CNBC) consistently says Fall 2026, meaning September-November at earliest",
      "logit": -3,
      "confidence": 0.95
    },
    {
      "description": "No pre-orders available from any OEM as of June 2, 2026; no official pricing announced by any OEM; no benchmarks shared \u2014 the product pipeline is demonstrably months from retail",
      "logit": -2.5,
      "confidence": 0.95
    },
    {
      "description": "Brand new silicon platform (first Nvidia ARM consumer chip for Windows) historically requires months of validation, driver maturation, and OEM QA before retail. The question's own description notes 'the typical gap is measured in months, not weeks'",
      "logit": -2,
      "confidence": 0.85
    },
    {
      "description": "The original N1/N1X launch was delayed ~1 year (from Q3 2025 to 2026) due to Windows on ARM readiness, memory supply issues, and silicon revisions \u2014 suggesting the ecosystem is not mature enough for surprise immediate retail",
      "logit": -1,
      "confidence": 0.7
    },
    {
      "description": "Lenovo Yoga Pro 7 appeared in Eastern European retailer database with specific prices (\u20ac3,199/\u20ac4,049), suggesting some OEM preparation may be more advanced than public messaging indicates \u2014 but no availability dates were listed",
      "logit": 0.3,
      "confidence": 0.3
    },
    {
      "description": "Pre-orders with binding payment and ship date \u2264 July 31 would count per resolution criteria \u2014 theoretically an OEM could open pre-orders during Computex week, though there is zero evidence this will happen",
      "logit": 0.2,
      "confidence": 0.15
    }
  ],
  "logit": -3.5,
  "probability": 0.03,
  "summary": "The Nvidia RTX Spark (N1/N1X) was officially unveiled at Computex on June 1, 2026, with ALL sources \u2014 Nvidia, Microsoft, every OEM partner, and all tech press \u2014 consistently stating \"Fall 2026\" availability. No pre-orders exist, no pricing has been announced, and no benchmarks have been shared, indicating the product pipeline is months from retail. The question asks about consumer purchase availability within ~12 days of announcement, which would be unprecedented for a brand-new silicon platform architecture. The only conceivable YES path would be a surprise pre-order opening with binding payment and a ship date before July 31, but there is zero evidence suggesting this will occur. I assign 3% probability, reflecting strong confidence in NO while maintaining a small floor for unknown unknowns."
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

## Forecast: Will any Nvidia N1/N1X-powered Windows PC be available for purchase by June 14, 2026?

**Probability: 3% (NO)**

### Key Findings

The Nvidia RTX Spark (the consumer branding for N1/N1X chips) was officially unveiled at Computex on June 1, 2026 — just yesterday. The evidence overwhelmingly points to NO:

1. **"Fall 2026" is universal**: Every single source — Nvidia, Microsoft, Dell, Lenovo, HP, ASUS, MSI, and all major tech press — consistently says systems will arrive in **Fall 2026** (September–November).

2. **No purchase pathway exists**: As of June 2, 2026:
   - Zero pre-orders available from any OEM
   - No official pricing announced by any OEM
   - No performance benchmarks shared (described as coming "closer to launch")

3. **Brand-new platform**: This is Nvidia's first-ever consumer ARM chip for Windows — a completely new architecture requiring months of driver maturation, software validation, and OEM quality assurance.

4. **Prior delays signal immaturity**: The platform was already delayed ~1 year (from Q3 2025) due to Windows on ARM readiness, memory supply issues, and silicon revisions.

5. **Historical precedent**: The gap between a Computex unveil of a new silicon platform and retail availability is consistently measured in months, not weeks. Even Snapdragon X Elite had pre-committed ship dates months before launch.

The only conceivable YES scenario — a surprise pre-order opening with binding payment and ship date ≤ July 31 — has zero supporting evidence.
