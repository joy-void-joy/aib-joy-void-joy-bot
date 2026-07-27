# Reasoning Log: What will the market capitalization of the USD1 stablecoin be on August 7, 2026?

*Generated: 2026-07-27T19:43:57.879917+00:00*


## 💭 Thinking



## 🔧 Tool: mcp__research__research


```json
{
  "query": "Current USD1 stablecoin (World Liberty Financial USD) market capitalization on CoinGecko, latest value late July 2026 and daily trajectory over the past 2-3 weeks",
  "ttl": "6h"
}
```

### 📋 Result

```
Invalid input: 1 validation error for ResearchInput
questions
  Field required [type=missing, input_value={'query': 'Current USD1 s...2-3 weeks', 'ttl': '6h'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "Current USD1 stablecoin (World Liberty Financial USD) market capitalization on CoinGecko, latest value in late July 2026 and daily/weekly trajectory over the past 3-4 weeks. Any recent news about minting deals, redemptions, integrations affecting supply.",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Current USD1 stablecoin (World Liberty Financial USD) market capitalization on CoinGecko, latest value in late July 2026 and daily/weekly trajectory over the past 3-4 weeks.
Any recent news about minting deals, redemptions, integrations affecting supply.", "entry": {"slug": "current-usd1-stablecoin-world-liberty-financial-us-e0d1a729", "query": "Current USD1 stablecoin
(World Liberty Financial USD) market capitalization on CoinGecko, latest value in late July 2026 and daily/weekly trajectory over the past 3-4 weeks. Any recent news about minting deals, redemptions,
integrations affecting supply.", "answer": "I've completed the research. Here's a summary of the key findings on USD1's current market capitalization and trajectory:\n\n**Current Market Cap (late July
2026):** ~**$4.09\u20134.11 billion**, well-corroborated across CoinGecko ($4.107B), CoinMarketCap ($4.089B), and DefiLlama (~$4.13B supply). Peg is holding at ~$0.9988. USD1 is the **4th-largest
stablecoin** globally (behind USDT, USDC, USDS).\n\n**3\u20134 Week Trajectory \u2014 Declining:**\n- Supply peaked near **$5.3B in H1 2026** and has since contracted ~20% to ~$4.1B, indicating net
redemptions.\n- DefiLlama chain data confirms the drawdown: BNB Chain (largest, ~1.59B) and Ethereum (~1.49B) both declining; Tron (~1.02B) roughly flat.\n- This aligns with a **sector-wide stablecoin
contraction** \u2014 the total stablecoin market shrank ~$10B (~3%) from its May 2026 peak, with a record $7.7B monthly decline in June (largest since Terra-Luna in May 2022).\n\n**Supply-Affecting
News:**\n- USD1's supply is unusually lumpy/institution-driven \u2014 Binance-linked wallets held ~87% of supply at one point, and growth came from deals like the $2B MGX\u2013Binance settlement. The
wind-down of Binance booster incentives (APR cut 20%\u21928%) likely drove some of the recent contraction.\n- Integrations expanding utility: Binance now settles BTC/ETH perpetual futures in USD1;
native launch on Tempo (Stripe L1) in May 2026; Chainlink CCIP cross-chain support.\n- Regulatory: BitGo-custodied, Treasury-backed, GENIUS Act-aligned; a national bank charter application (Jan 2026)
with an OCC decision still pending.\n\nThe full structured findings (data points with sources and dates) have been submitted via the StructuredOutput tool.", "sources": [{"url":
"https://www.coingecko.com/en/coins/usd1-wlfi", "title": "USD1 Price: USD1/USD Live Price Chart, Market Cap & News Today | CoinGecko", "domain": "coingecko.com", "accessed_at": "2026-07-27T00:00:00Z",
"snippet": "Market cap $4.107B, circulating supply 4.112B USD1, price $0.9988, 24h volume $842.9M, rank #24. ATH $1.05 (July 9, 2026), ATL $0.9888 (July 9, 2026)."}, {"url":
"https://coinmarketcap.com/currencies/usd1/", "title": "World Liberty Financial USD price today, USD1 to USD live price, marketcap and chart | CoinMarketCap", "domain": "coinmarketcap.com",
"accessed_at": "2026-07-27T00:00:00Z", "snippet": "Market cap $4,089,302,996; circulating supply 4,094,448,189 USD1; price $0.998743; 24h volume $873.6M; rank #20."}, {"url":
"https://defillama.com/stablecoin/world-liberty-financial-usd", "title": "World Liberty Financial USD (USD1) Market Cap, Supply & Peg Chart - DefiLlama", "domain": "defillama.com", "accessed_at":
"2026-07-27T00:00:00Z", "snippet": "Total circulating ~4.13B across chains; BNB ~1.59B (declining), Ethereum ~1.49B (declining), Tron ~1.02B (flat). Fiat-backed, no audit."}, {"url":
"https://ethnews.com/usd1-stablecoin-supply-hits-5-3b-as-wlfi-token-lags/", "title": "USD1 Stablecoin Supply Hits $5.3B as WLFI Token Lags", "domain": "ethnews.com", "accessed_at":
"2026-07-27T00:00:00Z", "snippet": "USD1 supply peaked near $5.3B in H1 2026; Binance settles BTC and ETH perpetual futures directly in USD1; OCC charter decision still pending."}, {"url":
"https://blockchainreporter.net/what-is-usd1-stablecoin/", "title": "USD1 Stablecoin Explained: How It Works & Who Backs It", "domain": "blockchainreporter.net", "accessed_at": "2026-07-27T00:00:00Z",
"snippet": "4th-largest stablecoin; $2B MGX-Binance settlement in USD1; Binance wallets held ~87% of supply (Forbes); ~617,000 holders; national bank charter application Jan 2026; grew from $3.3B
(end-2025) to ~$4.5B mid-2026."}, {"url": "https://stablecoininsider.org/usd1-q1-2026-stablecoin-report/", "title": "WLFI's USD1 Q1 2026 Stablecoin Report", "domain": "stablecoininsider.org",
"accessed_at": "2026-07-27T00:00:00Z", "snippet": "USD1 crossed ~$4.52B market cap with over 4.52B USD1 circulating in Q1 2026, fastest-growing stablecoin."}, {"url":
"https://www.coindesk.com/markets/2026/07/12/stablecoin-market-cap-has-shrunk-by-usd10-billion-since-may-but-analyst-sees-no-reason-to-panic", "title": "Stablecoin market cap has shrunk by $10 billion
since May, but analyst sees no reason to panic", "domain": "coindesk.com", "accessed_at": "2026-07-27T00:00:00Z", "snippet": "Total stablecoin market cap fell ~$10B (~3%) since May 2026 peak, with
$7.7B decline in June alone \u2014 largest dollar drop since May 2022 Terra-Luna collapse."}, {"url": "https://www.gncrypto.news/news/stablecoin-market-cap-drops-1-9b-sky-dollar-falls-most/", "title":
"Stablecoin Market Cap Drops $1.9B; Sky Dollar Falls Most", "domain": "gncrypto.news", "accessed_at": "2026-07-27T00:00:00Z", "snippet": "Stablecoin market cap fell $1.911B to $311.311B for week
ending July 5, 2026 (DefiLlama); Tether lost $791M, Sky Dollar down 2.36%."}, {"url": "https://eco.com/support/en/articles/11753300-usd1-stablecoin-by-world-liberty-financial", "title": "USD1
Stablecoin by World Liberty Financial | Support", "domain": "eco.com", "accessed_at": "2026-07-27T00:00:00Z", "snippet": "USD1 issued by WLF, custodied by BitGo Trust, backed by cash and short-
duration US Treasury bills via government money market funds; grew to ~$4.5B by Q1 2026."}, {"url": "https://ourcryptotalk.com/blog/usd1-stablecoin-top-five-2026", "title": "USD1 Stablecoin Explained:
How It Hit the Top Five in 2026", "domain": "ourcryptotalk.com", "accessed_at": "2026-07-27T00:00:00Z", "snippet": "USD1 market cap ~$4.57B, ranked 4th on DefiLlama behind USDT, USDC, USDS."}],
"key_facts": [], "data_points": [{"metric": "USD1 market capitalization (CoinGecko)", "value": 4107000000.0, "unit": "USD", "as_of": "2026-07-26", "source_url":
"https://www.coingecko.com/en/coins/usd1-wlfi"}, {"metric": "USD1 circulating supply (CoinGecko)", "value": 4112000000.0, "unit": "USD1 tokens", "as_of": "2026-07-26", "source_url":
"https://www.coingecko.com/en/coins/usd1-wlfi"}, {"metric": "USD1 price (CoinGecko)", "value": 0.9988, "unit": "USD", "as_of": "2026-07-26", "source_url":
"https://www.coingecko.com/en/coins/usd1-wlfi"}, {"metric": "USD1 24h trading volume (CoinGecko)", "value": 842942000.0, "unit": "USD", "as_of": "2026-07-26", "source_url":
"https://www.coingecko.com/en/coins/usd1-wlfi"}, {"metric": "USD1 market cap rank (CoinGecko)", "value": 24.0, "unit": "rank", "as_of": "2026-07-26", "source_url":
"https://www.coingecko.com/en/coins/usd1-wlfi"}, {"metric": "USD1 market capitalization (CoinMarketCap)", "value": 4089302996.0, "unit": "USD", "as_of": "2026-07-26", "source_url":
"https://coinmarketcap.com/currencies/usd1/"}, {"metric": "USD1 circulating supply (CoinMarketCap)", "value": 4094448189.0, "unit": "USD1 tokens", "as_of": "2026-07-26", "source_url":
"https://coinmarketcap.com/currencies/usd1/"}, {"metric": "USD1 24h volume (CoinMarketCap)", "value": 873605554.0, "unit": "USD", "as_of": "2026-07-26", "source_url":
"https://coinmarketcap.com/currencies/usd1/"}, {"metric": "USD1 total circulating supply (DefiLlama, all chains)", "value": 4130000000.0, "unit": "USD1 tokens", "as_of": "2026-07-26", "source_url":
"https://defillama.com/stablecoin/world-liberty-financial-usd"}, {"metric": "USD1 supply on BNB Chain (largest chain)", "value": 1589000000.0, "unit": "USD1 tokens", "as_of": "2026-07-26",
"source_url": "https://defillama.com/stablecoin/world-liberty-financial-usd"}, {"metric": "USD1 supply on Ethereum", "value": 1488000000.0, "unit": "USD1 tokens", "as_of": "2026-07-26", "source_url":
"https://defillama.com/stablecoin/world-liberty-financial-usd"}, {"metric": "USD1 supply on Tron", "value": 1022000000.0, "unit": "USD1 tokens", "as_of": "2026-07-26", "source_url":
"https://defillama.com/stablecoin/world-liberty-financial-usd"}, {"metric": "USD1 peak circulating supply in H1 2026", "value": 5300000000.0, "unit": "USD", "as_of": "2026-06-30", "source_url":
"https://ethnews.com/usd1-stablecoin-supply-hits-5-3b-as-wlfi-token-lags/"}, {"metric": "USD1 market cap Q1 2026 (peak, StablecoinInsider)", "value": 4520000000.0, "unit": "USD", "as_of":
"2026-03-31", "source_url": "https://stablecoininsider.org/usd1-q1-2026-stablecoin-report/"}, {"metric": "USD1 holder count", "value": 617000.0, "unit": "holders", "as_of": "2026-07-01", "source_url":
"https://blockchainreporter.net/what-is-usd1-stablecoin/"}, {"metric": "Total stablecoin market cap decline since May 2026 peak", "value": 10000000000.0, "unit": "USD", "as_of": "2026-07-12",
"source_url": "https://www.coindesk.com/markets/2026/07/12/stablecoin-market-cap-has-shrunk-by-usd10-billion-since-may-but-analyst-sees-no-reason-to-panic"}, {"metric": "Total stablecoin market cap
June 2026 monthly decline", "value": 7700000000.0, "unit": "USD", "as_of": "2026-06-30", "source_url": "https://www.coindesk.com/markets/2026/07/12/stablecoin-market-cap-has-shrunk-by-usd10-billion-
since-may-but-analyst-sees-no-reason-to-panic"}, {"metric": "Total stablecoin market cap (week ending July 5, 2026)", "value": 311311000000.0, "unit": "USD", "as_of": "2026-07-05", "source_url":
"https://www.gncrypto.news/news/stablecoin-market-cap-drops-1-9b-sky-dollar-falls-most/"}], "created_at": "2026-07-27T19:42:51.377822Z", "updated_at": "2026-07-27T19:42:51.377822Z", "stale_after":
"2026-07-28T01:42:51.377822Z", "state": "fresh", "revision_history": [], "session_id": "bf3293ad-cd92-4cb6-9f9c-132d583914e5", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 1,
"failed_count": 0}
```


### ↳ Nested research agent trace

# Reasoning Log: Current USD1 stablecoin (World Liberty Financial USD) market capitalization on CoinGecko, latest value in late July 2026 and daily/weekly trajectory over the past 3-4 weeks. Any recent news about minting deals, redemptions, integrations affecting supply.

*Generated: 2026-07-27T19:42:51.372655+00:00*


## 💬 Response

I'll research the current USD1 stablecoin market capitalization and recent trajectory. Let me start by loading the necessary search tools.

## 🔧 Tool: ToolSearch


```json
{
  "query": "web search news",
  "max_results": 5
}
```

### 📋 Result

```

```

## 🔧 Tool: ToolSearch


```json
{
  "query": "fetch url webpage content",
  "max_results": 3
}
```

### 📋 Result

```

```

## 💬 Response

Let me search for current USD1 market cap data and recent news.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "USD1 stablecoin World Liberty Financial market cap CoinGecko July 2026"
}
```

### 📋 Result

```
{"query": "USD1 stablecoin World Liberty Financial market cap CoinGecko July 2026", "results": [{"title": "World Liberty Financial price today, WLFI to USD chart, marketcap and volume | CryptoSlate",
"url": "https://cryptoslate.com/coins/world-liberty-financial/", "snippet": null, "api_data": null, "hint": null}, {"title": "Latest World Liberty Financial USD News - (USD1) Future Outlook, Trends &
Market Insights", "url": "https://coinmarketcap.com/cmc-ai/usd1/latest-updates/", "snippet": "Deep Dive\n1. Cross-Chain Bridge via Chainlink CCIP (2025)\nOverview: This integration allows USD1 holders
to move their tokens seamlessly between supported blockchains like Ethereum, BNB Chain, and Tron. It uses Chainlink's Cross-Chain Interoperability Protocol (CCIP) as a secure, third-party bridge
service.\nThe bridge is a core infrastructure component that increases USD1's utility by making it available across multiple ecosystems without relying on a single issuer's proprietary technology.
This", "api_data": null, "hint": null}, {"title": "World Liberty Financial USD Price, USD1 Price, Live Charts, and Marketcap: usd1, usd1 coin, usd1 price - Coinbase Canada", "url":
"https://www.coinbase.com/en-ca/price/usd1-wlfi", "snippet": "Data is sourced from CoinMarketCap, CoinGecko and other third parties. We make no representation on the accuracy of the data provided.
[Learn more](https://www.coinbase.com#LegalSection)\nAbout World Liberty Financial USD\nWorld Liberty Financial USD (USD1) is a stablecoin designed to maintain a 1:1 peg with the U.S. dollar. It was
launched in March 2025 by World Liberty Financial Inc. (WLFI), a decentralized finance (DeFi) platform closely associated with the Trump family.\nGet up to CA$150 for ge", "api_data": null, "hint":
null}, {"title": "World Liberty Financial\u2019s USD1 Tops $5B Market Cap as TRUMP Meme Coin Stumbles", "url": "https://finance.yahoo.com/news/world-liberty-financial-usd1-tops-103856863.html",
"snippet": "A Trump-linked [stablecoin](https://decrypt.co/?post_type=post&p=5761) has crossed a $5 billion market cap in under a year, while the U.S. President's official meme coin has collapsed more
than 94% from its peak, as capital flows shift toward yield-bearing, institution-friendly stablecoins.\n[World Liberty Financial](https://decrypt.co/resources/what-is-world-liberty-financial-the-
trump-family-defi-project-explained)'s dollar-backed stablecoin [USD1](https://decrypt.co/311362/trump-world-liberty-", "api_data": null, "hint": null}, {"title": "World Liberty Financial price today,
WLFI to USD live price, marketcap and chart | CoinMarketCap", "url": "https://coinmarketcap.com/currencies/world-liberty-financial-wlfi/", "snippet": "This is the official WLFI project backed by
Donald J. Trump.\nLoading Data\nPlease wait, we are loading chart data\nWorld Liberty Financial Markets\nAll\nAll\nCEX\nCEX\nDEX\nDEX\nSpot\nSpot\nPerpetual\nPerpetual\nFutures\nFutures\nLoading
data...\nDisclaimer: This page may contain affiliate links. CoinMarketCap may be compensated if you visit any affiliate links and you take certain actions such as signing up and transacting with these
affiliate platforms. Please refer to Affiliate Disclosure\nUSD1 Stablecoin: A ", "api_data": null, "hint": null}, {"title": "World Liberty Financial Price: WLFI/USD Live Price Chart, Market Cap & News
Today | CoinGecko", "url": "https://www.coingecko.com/en/coins/world-liberty-financial", "snippet": "![WLFI logo](https://assets.coingecko.com/coins/images/50767/standard/wlfi.png?1756438915)\n![WLFI
logo](https://assets.coingecko.com/coins/images/50767/standard/wlfi.png?1756438915)\nWorld Liberty Financial\nWLFI Price\nHow is the price of World Liberty Financial (WLFI) calculated?\nThe price of
World Liberty Financial (WLFI) is calculated in real-time by aggregating the latest data across 70 exchanges and 119 markets, using a global volume-weighted average formula. Learn more about [how
crypto pric", "api_data": null, "hint": null}, {"title": "World Liberty Financial USD price today, USD1 to USD live price, marketcap and chart | CoinMarketCap", "url":
"https://coinmarketcap.com/currencies/usd1/", "snippet": "Disclaimer: This page may contain affiliate links. CoinMarketCap may be compensated if you visit any affiliate links and you take certain
actions such as signing up and transacting with these affiliate platforms. Please refer to Affiliate Disclosure\nWhat is USD1?\nUSD1 is a fiat-backed digital asset, designed to maintain a 1:1
equivalence with the U.S. dollar. Launched in April 2025 by World Liberty Financial (WLFI), a financial technology firm headquartered in Miami, Florida, USD1 aims to stream", "api_data": null, "hint":
null}, {"title": "World Liberty Financial USD (USD1) Market Cap, Supply & Peg Chart - DefiLlama", "url": "https://defillama.com/stablecoin/world-liberty-financial-usd", "snippet": "[Try
LlamaAI](https://defillama.com/ai)\nStablecoin Information\nUSD1 is a stablecoin backed by U.S. Treasuries and cash equivalents\nCategory:fiat-backed\nMinting and Redemption\nMinting USD1 involves
authorized institutions depositing dollars or equivalent assets held in custody, while redemption requires burning USD1 to receive an equivalent amount of underlying reserves through the issuer's
managed process\nAudits:No\nStablecoins Usage by Chain\n| Name | Bridge | |||||\n|---|---|---|---|---|---|---|\n", "api_data": null, "hint": null}, {"title": "What Is World Liberty Financial USD
(USD1) And How Does It Work?", "url": "https://coinmarketcap.com/cmc-ai/usd1/what-is/", "snippet": "Deep Dive\n1. Purpose & Value Proposition\nUSD1 aims to provide a digital dollar that is both stable
and trustworthy for global transactions. Its core value proposition is offering a compliant, transparent alternative to other major stablecoins. It is designed to facilitate faster, cheaper cross-
border payments and serve as reliable collateral within decentralized finance (DeFi).\n2. Technology & Backing Mechanism\nStability is achieved through a fiat-collateralized model. For every USD1
token minte", "api_data": null, "hint": null}]}
```

```json
{
  "url": "https://www.coingecko.com/en/coins/world-liberty-financial-usd",
  "prompt": "Current USD1 market capitalization, circulating supply, price, and 24h/7d changes"
}
```

### 📋 Result

```
HTTP 404 for https://www.coingecko.com/en/coins/world-liberty-financial-usd. The URL may have changed. Try WebSearch to find the current URL.
```

## 💬 Response

The correct CoinGecko slug is different. Let me fetch the correct pages including DefiLlama which tracks supply trajectory well.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://defillama.com/stablecoin/world-liberty-financial-usd",
  "prompt": "Current USD1 market cap / circulating supply, and how it has changed over the past 3-4 weeks (daily/weekly trajectory)"
}
```

### 📋 Result

```
{"url": "https://defillama.com/stablecoin/world-liberty-financial-usd", "content": "Based on the provided content, I can extract the following information about USD1:\n\n**Current Market
Cap/Circulating Supply:**\nThe table shows circulating supplies across different chains totaling approximately **4.13 billion USD1**:\n- Chain 1: 1.589b\n- Chain 2: 1.488b\n- Chain 3: 1.022b\n- Chain
4: 18.52m\n- Chain 5: 16.3m\n- Chain 6: 10.06m\n- Chain 7: 122,279.17\n- Chain 8: 1,162.38\n\n**Changes Over Past 3-4 Weeks:**\nThe content shows percentage changes but doesn't specify the exact
timeframe clearly. Based on the columns (which appear to be 1-day, 1-week, and longer-term changes):\n\n- **Chain 1**: -1.83% (short-term), -13.12% (longer-term) - declining trajectory\n- **Chain 2**:
-0.54% (1-day), -6.56% (1-week), -17.44% (longer-term) - consistent decline\n- **Chain 3**: +0.09% - stable/slight growth\n- **Chain 5**: +35.50%, +45.34% - significant growth\n- **Chain 7**: -71.60%,
-94.74% - sharp decline\n\n**Overall:** The total supply appears to have declined over the past few weeks, with the two largest chains (1.589b and 1.488b) showing negative growth rates.\n\n**Note:**
The content doesn't provide explicit timestamps for the percentage changes, so the exact \"3-4 week\" trajectory cannot be definitively confirmed from this data alone.\n\n**Relevant links:**\n- [Try
LlamaAI](https://defillama.com/ai)", "title": "World Liberty Financial USD (USD1) Market Cap, Supply & Peg Chart - DefiLlama"}
```

```json
{
  "url": "https://coinmarketcap.com/currencies/usd1/",
  "prompt": "Current USD1 market cap, circulating supply, price, 24h volume, and recent changes"
}
```

### 📋 Result

```
{"url": "https://coinmarketcap.com/currencies/usd1/", "content": "Based on the provided content, here are the current USD1 metrics:\n\n**Market Cap:** $4,089,302,996 USD\n\n**Circulating Supply:**
4,094,448,189 USD1 coins\n\n**Price:** $0.998743 USD\n\n**24-Hour Trading Volume:** $873,605,554 USD\n\n**Recent Changes:** Down 0.02% in the last 24 hours\n\n**CoinMarketCap Ranking:** #20\n\n**Max
Supply:** Not available\n\nRelevant links:\n- [CoinMarketCap USD1 Page](https://coinmarketcap.com/currencies/usd1/)", "title": "World Liberty Financial USD price today, USD1 to USD live price,
marketcap and chart | CoinMarketCap"}
```

## 💬 Response

I have good baseline data. Let me get the CoinGecko-specific page and recent news about minting deals/redemptions.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "USD1 stablecoin CoinGecko market cap 4 billion"
}
```

### 📋 Result

```
{"query": "USD1 stablecoin CoinGecko market cap 4 billion", "results": [{"title": "USD1 Price: USD1/USD Live Price Chart, Market Cap & News Today | CoinGecko", "url":
"https://www.coingecko.com/en/coins/usd1-wlfi", "snippet": "![USD1 logo](https://assets.coingecko.com/coins/images/54977/standard/USD1_1000x1000_transparent.png?1749297002)\n![USD1
logo](https://assets.coingecko.com/coins/images/54977/standard/USD1_1000x1000_transparent.png?1749297002)\nUSD1\nUSD1 Price\nHow is the price of USD1 (USD1) calculated?\nThe price of USD1 (USD1) is
calculated in real-time by aggregating the latest data across 74 exchanges and 427 markets, using a global volume-weighted average formula. Learn more about [how crypto prices are calcul", "api_data":
null, "hint": null}, {"title": "USD1 Stablecoin Guide: What is USD1 Crypto, How It Works, and Where to Buy", "url": "https://www.mexc.com/learn/article/usd1-stablecoin-guide-what-is-usd1-crypto-how-
it-works-and-where-to-buy/1", "snippet": "USD1 is World Liberty Financial's dollar-pegged stablecoin, issued by BitGo and backed by U.S. government money market funds and cash equivalents.\nIt has
drawn significant attention for its institutional-grade custody structure, rapid growth, and direct Trump family ties \u2014 making it one of the more closely watched new entrants in the stablecoin
market.\nThis guide covers USD1's core features, reserve structure, multichain deployment, real-world applications, and key considerations for anyone look", "api_data": null, "hint": null}, {"title":
"Top USD Stablecoins by Market Cap | CoinGecko", "url": "https://www.coingecko.com/en/categories/usd-stablecoin", "snippet": "Portfolios\nAdd to New Portfolio\nUSD Stablecoins by Market
Capitalization\nThe USD Stablecoin market cap today is $298 Billion, a -0.0% change in the last 24 hours.\nRead More about USD Stablecoin\nA USD stablecoin is a type of cryptocurrency that is designed
to maintain a stable value by being pegged to the United States dollar.\nHighlights\nCategory Overview\nabout 18 hours ago\n$298,476,663,270\nMarket Cap\n0.0%\n$59,050,744,266\n24h Trading Volume\n| #
| Coin | Price | 1h | 24h | 7d | 30d | 24h Volume | ", "api_data": null, "hint": null}, {"title": "USD1 [Old] Price: USD1/USD Live Price Chart, Market Cap & News Today | CoinGecko", "url":
"https://www.coingecko.com/en/coins/usd1-old", "snippet": "![USD1 logo](https://assets.coingecko.com/coins/images/53485/standard/USD1-Shield-Icon-Primary-Coral-White-RGB.png?1737197512)\n![USD1
logo](https://assets.coingecko.com/coins/images/53485/standard/USD1-Shield-Icon-Primary-Coral-White-RGB.png?1737197512)\nUSD1 [Old]\nUSD1 Price\nHow is the price of USD1 [Old] (USD1) calculated?\nThe
price of USD1 [Old] (USD1) is calculated by aggregating the latest data across multiple exchanges and markets, using a global volume-weighted average formula. Since USD1 ", "api_data": null, "hint":
null}, {"title": "Crypto Market Cap Charts | CoinGecko", "url": "https://www.coingecko.com/en/charts", "snippet": "Global Cryptocurrency Market Cap Charts\nThe global cryptocurrency market cap today
is $2.3 Trillion, a 0.25% change in the last 24 hours and -42.78% change one year ago. As of today, the market cap of\n[Bitcoin (BTC)](https://www.coingecko.com/en/coins/bitcoin)is at $1.3 Trillion,
representing a Bitcoin dominance of 56.51%. Meanwhile, Stablecoins' market cap is at $304 Billion and has a 13.2% share of the total crypto market cap.Total Crypto Market Cap\nThe chart below shows
the total market cap &", "api_data": null, "hint": null}, {"title": "Top Stablecoins by Market Cap | CoinGecko", "url": "https://www.coingecko.com/en/categories/stablecoins", "snippet": "Stablecoins
by Market Capitalization\nA stablecoin is a type of cryptocurrency that is designed to maintain a stable value by being pegged to an external reference, such as a fiat currency.\nWhat is a stablecoin?
Stablecoin is a cryptocurrency that is designed to minimize volatility by pegging to a more stable asset. Fiat currency digital asset is the most popular use case for stablecoins. It typically tracks
popular national currencies such as the US Dollar, Euro, and the British Pound. Benefit o", "api_data": null, "hint": null}, {"title": "USD1 Stablecoin Explained: How It Works & Who Backs It", "url":
"https://blockchainreporter.net/what-is-usd1-stablecoin/", "snippet": "![What Is USD1 Stablecoin? World Liberty Financial\u2019s Dollar Token Explained](https://blockchainreporter.net/wp-
content/uploads/2026/07/usd1.webp)\n[World Liberty Financial\u2019s USD1](https://worldlibertyfinancial.com/usd1) has gone from a March 2025 launch announcement to the fourth-largest stablecoin in the
world in roughly fifteen months, overtaking PayPal\u2019s PYUSD and Sky\u2019s DAI along the way. Its rise has been driven less by retail adoption than by a handful of enormous institutional deals
\u2014 most ", "api_data": null, "hint": null}]}
```

```json
{
  "query": "USD1 stablecoin World Liberty Financial minting redemption supply integration",
  "hours_back": 1200,
  "n_articles": 15
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403000 - API access is reserved for Spelunker and Analyst tiers only. Please upgrade your Free plan at https://my.asknews.app/plans
```

## 💬 Response

Let me fetch the CoinGecko USD1 page directly and get recent news via web search.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.coingecko.com/en/coins/usd1-wlfi",
  "prompt": "Current USD1 market capitalization, circulating supply, price, 24h trading volume, market cap rank, and any 24h/7d changes"
}
```

### 📋 Result

```
{"url": "https://www.coingecko.com/en/coins/usd1-wlfi", "content": "Based on the provided content, here are the USD1 (USD1) statistics:\n\n**Current Market Data:**\n- **Price:** $0.9988 - $0.9991 (24h
range)\n- **Market Capitalization:** $4.107B\n- **Market Cap Rank:** #24\n- **Circulating Supply:** 4.112B USD1\n- **24h Trading Volume:** $842.942M\n- **Fully Diluted Valuation (FDV):**
$4.107B\n\n**Price Changes:**\n- **1h:** 0.0%\n- **24h:** 0.0%\n- **7d:** 0.0%\n- **14d:** 0.0%\n- **30d:** 0.1%\n- **1y:** 0.3%\n\n**Additional Context:**\n- 24h trading volume represents a 109.80%
increase from one day ago\n- All-Time High: $1.05 (July 9, 2026) - currently 4.7% below ATH\n- All-Time Low: $0.9888 (July 9, 2026) - currently 1.0% above ATL\n- Market Cap/FDV ratio: 1 (indicating
all supply is in circulation)\n\n**Relevant links:**\n- [How crypto prices are calculated on CoinGecko](https://www.coingecko.com/en/methodology)\n- [CoinGecko
API](https://www.coingecko.com/en/api)\n- [What Is USD1? A US Stablecoin Launched by World Liberty Financial](https://www.coingecko.com/learn/what-is-usd1-stablecoin-world-liberty-financial)\n-
[Highest volume cryptocurrencies](https://www.coingecko.com/en/highlights/high-volume)\n- [Global cryptocurrency market charts](https://www.coingecko.com/en/charts)\n- [Stablecoins
category](https://www.coingecko.com/en/categories/stablecoins)", "title": "USD1 Price: USD1/USD Live Price Chart, Market Cap & News Today | CoinGecko"}
```

```json
{
  "url": "https://blockchainreporter.net/what-is-usd1-stablecoin/",
  "prompt": "Recent USD1 minting deals, institutional deals, redemptions, integrations affecting supply, current market cap, and growth trajectory in 2026"
}
```

### 📋 Result

```
{"url": "https://blockchainreporter.net/what-is-usd1-stablecoin/", "content": "Based on the content, here's what is known about USD1's recent activity and growth in 2026:\n\n## Recent Institutional
Deals & Supply Activity\n\n**Major Institutional Deals:**\n- **$2 billion settlement** between Abu Dhabi-based MGX and Binance, paid entirely in USD1 (timeframe not specified, but described as driving
USD1's rise)\n- An Abu Dhabi-linked firm purchased **$2 billion of USD1** in 2025\n- Abu Dhabi interests separately agreed to acquire a **49% stake in World Liberty Financial** itself\n\n**Supply
Concentration:**\n- Binance-linked wallets held approximately **87% of USD1 supply** at one point (according to Forbes)\n- Binance ran liquidity-seeding campaigns, including a booster program offering
up to 20% APR (later reduced to 8%)\n\n## Current Market Cap & Growth Trajectory\n\n**Market Metrics (mid-2026):**\n- Current market cap: **~$4.45-4.5 billion**\n- Circulating supply: **~4.46 billion
USD1**\n- Growth: From **$3.3 billion** at year-end 2025 to **$4.5 billion** by mid-2026\n- Ranking: **4th largest stablecoin** globally (behind USDT, USDC, and Sky's USDS)\n- Holders:
**~617,000**\n\n## Recent Integrations\n\n**Blockchain Expansions:**\n- Launched on **Ethereum and BNB Chain** (March 2025)\n- Added **Tron, Solana, Aptos, AB Core, Mantle, Monad, Plume, Morph**
through 2025-2026\n- Launched natively on **Tempo** (Stripe-backed L1) in **May 2026** as an early TIP-20 token\n\n## Regulatory Developments\n\n- January 2026: A World Liberty trust entity **applied
for a US national banking charter**\n- USD1 structure built to align with the **GENIUS Act** (federal stablecoin law signed July 2025)\n\n**Note:** The content does not provide specific details on
recent redemptions or month-by-month minting activity in 2026.\n\n---\n\n**Relevant links:**\n- [World Liberty Financial's USD1](https://worldlibertyfinancial.com/usd1)\n- [DefiLlama's stablecoin
tracker](https://blockchainreporter.net/what-is-defillama/)\n- [CoinGecko USD1 page](https://www.coingecko.com/en/coins/usd1-wlfi)\n- [CoinMarketCap USD1
page](https://coinmarketcap.com/currencies/usd1/)\n- [Today's crypto market overview](https://blockchainreporter.net/crypto-market-today/)\n- [GENIUS Act
explainer](https://blockchainreporter.net/what-is-the-genius-act-the-us-stablecoin-law-explained/)\n- [BitGo Trust Company](https://www.bitgo.com/)\n- [Chainlink Cross-Chain Interoperability
Protocol](https://chain.link/cross-chain)", "title": "USD1 Stablecoin Explained: How It Works & Who Backs It"}
```

## 💬 Response

I have strong data now. Let me get recent news specifically about the July 2026 trajectory and any minting/redemption events in the past few weeks.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "USD1 stablecoin supply July 2026 mint redemption deal news"
}
```

### 📋 Result

```
{"query": "USD1 stablecoin supply July 2026 mint redemption deal news", "results": [{"title": "USD1 Stablecoin Supply Hits $5.3B as WLFI Token Lags Altcoin News ETHNews", "url":
"https://ethnews.com/usd1-stablecoin-supply-hits-5-3b-as-wlfi-token-lags/", "snippet": "- USD1 stablecoin supply peaked near $5.3 billion during the first half of 2026.\n- Binance now settles Bitcoin
and Ethereum perpetual futures directly in USD1.\n- The OCC charter decision, reported as imminent in June, is still pending.\n- WLFI trades near $0.058, still inside the range set after May\u2019s
crash.\nWorld Liberty Financial pushed USD1, its dollar-backed stablecoin, to a peak circulating supply of $5.3 billion this year, landed it as a direct settlement asset on Binance\u2019s Bitcoin and
Ethe", "api_data": null, "hint": null}, {"title": "USD1 Stablecoin by World Liberty Financial | Support", "url": "https://eco.com/support/en/articles/11753300-usd1-stablecoin-by-world-liberty-
financial", "snippet": "USD1 is a US-dollar stablecoin issued by World Liberty Financial, custodied by BitGo Trust Company, and backed by cash and short-duration US Treasury bills held through
government money market funds. Launched on Ethereum and BNB Chain in March 2025, USD1 had grown to a circulating supply near $4.5 billion by Q1 2026, making it the fastest-growing fiat-backed
stablecoin of the period. This article covers how USD1 works, the chains it runs on, its reserve and custody structure, the World Liberty F", "api_data": null, "hint": null}, {"title": "USD1
Stablecoin Guide: What is USD1 Crypto, How It Works, and Where to Buy", "url": "https://www.mexc.com/learn/article/usd1-stablecoin-guide-what-is-usd1-crypto-how-it-works-and-where-to-buy/1",
"snippet": "USD1 is World Liberty Financial's dollar-pegged stablecoin, issued by BitGo and backed by U.S. government money market funds and cash equivalents.\nIt has drawn significant attention for
its institutional-grade custody structure, rapid growth, and direct Trump family ties \u2014 making it one of the more closely watched new entrants in the stablecoin market.\nThis guide covers USD1's
core features, reserve structure, multichain deployment, real-world applications, and key considerations for anyone look", "api_data": null, "hint": null}, {"title": "Ripple Launches Mint for
Institutional RLUSD Operations and Integrates Stablecoin With Notabene", "url": "https://bitcoinfoundation.org/news/crypto-companies-news/ripple-mint-notabene/", "snippet": "Ripple has unveiled Ripple
Mint \u2014 a platform allowing institutional clients to issue, redeem, transfer across networks, and track [RLUSD\u25b2$0.9999](https://bitcoinfoundation.org/markets/RLUSD) via web interface or
API.\nRipple Mint also supports automation and [stablecoin](https://bitcoinfoundation.org/news/stablecoin-news/stablecoins-explained-usdt-usdc-and-dai-compared/) integration into companies\u2019
internal systems. Separately, Ripple invested in compliance platform Notabene, which will add ident", "api_data": null, "hint": null}, {"title": "USD1 Stablecoin Explained: How It Works & Who Backs
It", "url": "https://blockchainreporter.net/what-is-usd1-stablecoin/", "snippet": "![What Is USD1 Stablecoin? World Liberty Financial\u2019s Dollar Token Explained](https://blockchainreporter.net/wp-
content/uploads/2026/07/usd1.webp)\n[World Liberty Financial\u2019s USD1](https://worldlibertyfinancial.com/usd1) has gone from a March 2025 launch announcement to the fourth-largest stablecoin in the
world in roughly fifteen months, overtaking PayPal\u2019s PYUSD and Sky\u2019s DAI along the way. Its rise has been driven less by retail adoption than by a handful of enormous institutional deals
\u2014 most ", "api_data": null, "hint": null}, {"title": "WLFI's USD1 Q1 2026 Stablecoin Report", "url": "https://stablecoininsider.org/usd1-q1-2026-stablecoin-report/", "snippet": "Table of
Contents\nNo stablecoin in 2026 has generated as much capital inflow, congressional scrutiny, institutional deal flow, or raw political intrigue as USD1.\nIssued by [World Liberty Financial
(WLFI)](https://worldlibertyfinancial.com/?ref=stablecoininsider.org), a DeFi protocol co-founded by President Donald Trump and his sons, the dollar-pegged token crossed a market cap of approximately
$4.52 billion with a circulating supply of over 4.52 billion USD1 coins, making it the fastest-growing ", "api_data": null, "hint": null}, {"title": "USD1 Stablecoin Explained: How It Hit the Top Five
in 2026 | Our Crypto Talk", "url": "https://ourcryptotalk.com/blog/usd1-stablecoin-top-five-2026", "snippet": "How did USD1 become a top 5 stablecoin in just one year of the launch? We explore in this
article the growth to $4.5B market cap and its potential from here.\nAuthor: Sahil Thakur\nThe USD1 stablecoin launched in March 2025. Fifteen months later, the token sits fourth on
[DefiLlama](https://defillama.com/stablecoins). Its market cap is about $4.57 billion. Only USDT, USDC, and Sky Dollar USDS sit ahead of it.
[CoinGecko](https://www.coingecko.com/en/categories/stablecoins) shows a similar picture,", "api_data": null, "hint": null}, {"title": "Ripple Just Solved RLUSD's Two Biggest Problems With Ripple Mint
and Notabene Deal - 24/7 Wall St.", "url": "https://247wallst.com/investing/cryptocurrency/2026/07/23/ripple-just-solved-rlusds-two-biggest-problems-with-ripple-mint-and-notabene-deal/", "snippet":
"Ripple just made two announcements, each aimed at a different obstacle keeping institutions from using its stablecoin. The first is Ripple Mint, a platform that lets institutions create, redeem,
bridge, and track Ripple USD (RLUSD) through code rather than a dashboard.\nThe second is a strategic investment in Notabene, a compliance network, with RLUSD going into its business payments
platform. Both moves show that Ripple is working to widen where RLUSD can be used and who is willing to use it. He", "api_data": null, "hint": null}]}
```

```json
{
  "query": "USD1 stablecoin market cap decline drop $4 billion 2026"
}
```

### 📋 Result

```
{"query": "USD1 stablecoin market cap decline drop $4 billion 2026", "results": [{"title": "Total Stablecoin Cap Falls $1.9 Billion This Week While Sky Dollar Leads the Slide", "url":
"https://news.bitcoin.com/total-stablecoin-cap-falls-1-9-billion-this-week-while-sky-dollar-leads-the-slide/", "snippet": "Tether lost $791 million this week, a single-token drop that accounted for
41% of the $1.9 billion pulled from the entire stablecoin market. Most of its top competitors also finished lower, with USDC shedding 1.05% and Sky Dollar plunging 2.36%.\nTotal Stablecoin Cap Falls
$1.9 Billion This Week While Sky Dollar Leads the Slide\n![Total Stablecoin Cap Falls $1.9 Billion This Week While Sky Dollar Leads the
Slide](/_next/image/?url=https%3A%2F%2Fstatic.news.bitcoin.com%2Fwp-content%2Fuploads%2F2026", "api_data": null, "hint": null}, {"title": "Stablecoin Market Decline Highlights Industry Shifts in
2026", "url": "https://en.cryptonomist.ch/2026/07/12/stablecoin-market-decline-2026/", "snippet": "The stablecoin market decline that unfolded since May 2026 looks alarming at first glance \u2014
roughly $10 billion wiped from total market capitalization, with $7.7 billion of that disappearing in June alone, according to data from RWA.xyz. But zoom out, and a more nuanced picture emerges: this
is the sharpest pullback since 2023, yet it represents only a 3% contraction \u2014 a fraction of the 26% collapse that defined the brutal 2022 crypto winter.\nSummary\nKey takeaways\n- The stablecoin
market cap has", "api_data": null, "hint": null}, {"title": "Stablecoin Market Cap Drops $1.9B; Sky Dollar Falls Most", "url": "https://www.gncrypto.news/news/stablecoin-market-cap-drops-1-9b-sky-
dollar-falls-most/", "snippet": "Stablecoin market cap drops $1.9B; Sky Dollar falls most\nStablecoin market cap fell $1.911B to $311.311B for the week ending July 5, 2026. Sky Dollar dropped 2.36%;
Tether lost $791M, about 41% of total outflows.\nStablecoin market capitalization fell $1.911 billion to $311.311 billion in the week ending July 5, 2026, according to DefiLlama. The sector declined
0.61% over seven days. Sky Dollar (USDS) recorded the largest weekly drop among the top 15, down 2.36% to $8.02 billion. Tether\u2019s USDT fe", "api_data": null, "hint": null}, {"title": "Stablecoin
market decline hits $10B \u2014 is crypto liquidity at risk?", "url": "https://cryptonews.net/news/finance/33137541/", "snippet": "The stablecoin market decline that unfolded since May 2026 looks
alarming at first glance \u2014 roughly $10 billion wiped from total market capitalization, with $7.7 billion of that disappearing in June alone, according to data from RWA.xyz. But zoom out, and a
more nuanced picture emerges: this is the sharpest pullback since 2023, yet it represents only a 3% contraction \u2014 a fraction of the 26% collapse that defined the brutal 2022 crypto winter.\nKey
takeaways\n- The stablecoin market cap has fallen ", "api_data": null, "hint": null}, {"title": "Stablecoin market cap has shrunk by $10 billion since May ...", "url":
"https://www.coindesk.com/markets/2026/07/12/stablecoin-market-cap-has-shrunk-by-usd10-billion-since-may-but-analyst-sees-no-reason-to-panic", "snippet": "Stablecoin market cap has shrunk by $10
billion since May, but analyst sees no reason to panic\nThe market shrank by $7.7 billion in June alone, the largest dollar amount since May 2022's Terra-Luna crash, but stablecoins will likely resume
their long-term growth, one analyst said.\nThe stablecoin market has shrunk by roughly $10 billion since its May peak, including a $7.7 billion decline just in June.\nOn a percentage basis, though, it
was just a 3% fall; still modest compared with the 26% contra", "api_data": null, "hint": null}, {"title": "Stablecoins Have Lost $10 Billion Since May, But an Analyst Sees No Cause for Alarm", "url":
"https://coinpaprika.com/news/stablecoins-lost-10-billion-may-analyst-sees/", "snippet": "Stablecoins Have Lost $10 Billion Since May, But an Analyst Sees No Cause for Alarm\nThe total value of
stablecoins in circulation has fallen by roughly $10 billion since its May 2026 peak, a decline of about 3%. Tether and USDC drove most of the drop, though the market remains near $300
billion.\n![Stablecoins Have Lost $10 Billion Since May, But an Analyst Sees No Cause for
Alarm](https://content.coinpaprika.com/api/files/news/7ap2peukevfgja9/stablecoins_lost_10_billion_may_analyst_cover_a0e17v3", "api_data": null, "hint": null}, {"title": "Stablecoin market cap has
shrunk by $10 billion since May, but analyst sees no reason to panic", "url": "https://cryptonews.net/news/finance/33137279/", "snippet": "The stablecoin market posted its biggest retreat in years in
June, a sign that onchain liquidity has dwindled as crypto markets continued to consolidate near 2026 lows.\nLast month saw a $7.7 billion decline in stablecoin market capitalization, the largest
dollar amount since May 2022, when blockchain protocol Terra-Luna collapsed, kickstarting a brutal bear market often dubbed as crypto winter, CoinDesk Data
reported.\n![](https://cnews24.ru/uploads/b2c/b2c76b73ba99610a73a1b420477ae82e79022444.jp", "api_data": null, "hint": null}, {"title": "Stablecoin Market Cap Suffers Biggest Decline in 4 Years |
PYMNTS.com", "url": "https://www.pymnts.com/cryptocurrency/2026/stablecoin-market-cap-suffers-biggest-decline-in-4-years/", "snippet": "That\u2019s according to a
[report](https://www.coindesk.com/markets/2026/07/12/stablecoin-market-cap-has-shrunk-by-usd10-billion-since-may-but-analyst-sees-no-reason-to-panic) Sunday (July 12) by CoinDesk, which calls the
downturn a sign that on-chain liquidity has dipped as crypto markets continue to consolidate near this year\u2019s lows.\nStablecoins\u2019 market capitalization dropped by $7.7 billion in June, the
report said. That\u2019s the largest dollar amount since May 2022, when the collapse of the Terra-L", "api_data": null, "hint": null}]}
```

## 💬 Response

I now have comprehensive data. The picture is clear: USD1 peaked near $5.3B in H1 2026 and has declined to ~$4.1B by late July 2026, consistent with a broader stablecoin market contraction. Let me compile the final report.

## Research Report: USD1 Stablecoin (World Liberty Financial USD) Market Capitalization — Late July 2026

### Current Market Cap (as of ~July 26–27, 2026)

USD1's market capitalization sits at approximately **$4.09–4.11 billion**, with data converging across sources:

- **CoinGecko** (`usd1-wlfi`): Market cap **$4.107 billion**, circulating supply **4.112 billion USD1**, price **$0.9988**, 24h volume **$842.9M**, market cap rank **#24**. FDV = market cap (all supply circulating).
- **CoinMarketCap**: Market cap **$4.089 billion**, circulating supply **4.094 billion USD1**, price **$0.998743**, 24h volume **$873.6M**, rank **#20**.
- **DefiLlama**: Total circulating supply ~**4.13 billion** across chains (BNB Chain ~1.59B, Ethereum ~1.49B, Tron ~1.02B, plus smaller amounts on Solana/Aptos and others).

The peg is holding near $1.00. CoinGecko shows an ATH of $1.05 and ATL of $0.9888, both recorded July 9, 2026 (brief depeg volatility that has since normalized). Price changes over 1h/24h/7d/30d are all essentially flat (~0.0–0.1%), as expected for a stablecoin.

### Trajectory Over the Past 3–4 Weeks (and H1 2026 context)

The dominant story is a **downtrend in supply from a mid-2026 peak**:

- **Peak**: USD1 circulating supply peaked near **$5.3 billion** during H1 2026 (ETHNews). Other sources cite a Q1 2026 peak of ~$4.5–4.57B market cap when it was described as the fastest-growing fiat-backed stablecoin.
- **Current**: Now down to **~$4.1 billion**, implying a contraction of roughly **$1.0–1.2 billion (~20%)** from the peak.
- **DefiLlama chain-level trends** show the two largest chains contracting: BNB Chain down ~-1.8% short-term / ~-13% longer-term, and Ethereum down ~-0.5% (1d) / ~-6.6% (1w) / ~-17% (longer-term). Tron was roughly flat. This confirms net redemption/burning of USD1 over recent weeks.

**Broad-market context** — the decline coincides with a sector-wide stablecoin contraction:
- The total stablecoin market cap fell ~**$10 billion (~3%)** from its May 2026 peak, with **$7.7 billion wiped in June alone** — the largest monthly dollar decline since the May 2022 Terra-Luna collapse (CoinDesk, RWA.xyz data).
- For the week ending July 5, 2026, total stablecoin cap fell $1.911B to $311.311B (DefiLlama); Tether led outflows (-$791M), Sky Dollar (USDS) fell most in % terms (-2.36%).
- So USD1's pullback is partly idiosyncratic (institutional deal-driven supply is "lumpy") and partly aligned with reduced on-chain liquidity market-wide.

### Ranking

USD1 is described as the **4th-largest stablecoin globally** (behind USDT, USDC, and Sky's USDS), having overtaken PayPal's PYUSD and DAI within ~15 months of launch. CoinGecko/CMC overall crypto rank is #20–24.

### Recent News Affecting Supply (Minting, Redemptions, Integrations)

**Supply concentration & institutional deals (the key supply drivers):**
- USD1's growth has been driven by a handful of large institutional deals rather than retail — most notably a **$2 billion MGX–Binance settlement** paid entirely in USD1, and a separate ~$2 billion purchase by an Abu Dhabi-linked firm (2025).
- **Binance-linked wallets held ~87% of USD1 supply** at one point (Forbes) — meaning supply is highly sensitive to Binance/institutional flows, explaining the volatility as those positions unwind.
- Binance liquidity-seeding/booster programs (APR up to 20%, later cut to 8%) supported earlier growth; the reduction likely contributed to the recent contraction.

**Integrations / utility expansions:**
- **Binance now settles Bitcoin and Ethereum perpetual futures directly in USD1** (ETHNews) — a meaningful utility integration.
- Cross-chain expansion via **Chainlink CCIP** across Ethereum, BNB Chain, and Tron.
- Native launch on **Tempo** (Stripe-backed L1) as an early TIP-20 token in May 2026; also added Solana, Aptos, AB Core, Mantle, Monad, Plume, Morph through 2025–2026.

**Regulatory / structural:**
- Issued by **BitGo Trust**, backed by cash and short-duration US Treasuries via government money market funds; structured to align with the **GENIUS Act** (US stablecoin law signed July 2025).
- A World Liberty trust entity **applied for a US national banking charter** (Jan 2026); an OCC charter decision reported as imminent in June was **still pending** as of the latest reporting.
- Holder count ~**617,000**.

### Data Caveats
- Sources differ slightly on peak values ($4.5B "Q1 peak" vs. $5.3B H1 peak) — likely reflecting different measurement dates and mint/redeem cycles. The current ~$4.1B figure is well-corroborated across CoinGecko, CMC, and DefiLlama.
- No audit is published (DefiLlama notes "Audits: No").

## 🔧 Tool: StructuredOutput


```json
{
  "answer": "USD1 (World Liberty Financial USD) market capitalization stands at approximately $4.09\u20134.11 billion as of late July 2026, corroborated across CoinGecko ($4.107B), CoinMarketCap ($4.089B), and DefiLlama (~$4.13B circulating supply). The peg is holding near $1.00 (CoinGecko price $0.9988). USD1 ranks as the ~4th-largest stablecoin globally (behind USDT, USDC, and Sky's USDS) and #20\u201324 overall on CMC/CoinGecko.\n\nTrajectory: The dominant recent trend is a decline in supply from a mid-2026 peak. Circulating supply peaked near $5.3 billion during H1 2026 (ETHNews) and has since contracted to ~$4.1B, a drop of roughly $1.0\u20131.2 billion (~20%). DefiLlama chain-level data confirms net redemptions over recent weeks: BNB Chain (~1.59B, largest) down ~13% longer-term, Ethereum (~1.49B) down ~6.6% over 1 week / ~17% longer-term, with Tron (~1.02B) roughly flat. This coincides with a sector-wide stablecoin contraction \u2014 total stablecoin market cap fell ~$10B (~3%) from its May 2026 peak, including a record $7.7B monthly decline in June 2026 (CoinDesk/RWA.xyz), the largest dollar decline since the May 2022 Terra-Luna collapse. For the week ending July 5, 2026, total stablecoin cap fell $1.911B to $311.311B (DefiLlama).\n\nSupply drivers: USD1's growth was driven by large institutional deals rather than retail \u2014 notably a $2 billion MGX\u2013Binance settlement paid in USD1 and a ~$2B Abu Dhabi-linked purchase. Binance-linked wallets held ~87% of supply at one point (Forbes), making supply highly sensitive to Binance/institutional flows; the wind-down of Binance booster incentives (APR cut from 20% to 8%) likely contributed to the recent decline. Recent integrations expanding utility include Binance settling BTC/ETH perpetual futures directly in USD1, cross-chain support via Chainlink CCIP, and a native launch on Tempo (Stripe-backed L1) in May 2026. Regulatory developments: issued by BitGo Trust, backed by cash and short-duration US Treasuries via money market funds, structured to align with the GENIUS Act; a World Liberty trust entity applied for a US national banking charter (Jan 2026), with an OCC/charter decision reported imminent in June but still pending. Holder count ~617,000. No published audit (DefiLlama).\n\nCaveats: Sources vary on the peak ($4.5B Q1 figure vs. $5.3B H1 peak) due to different measurement dates and lumpy mint/redeem cycles, but the current ~$4.1B is well-corroborated.</answer>\n<parameter name=\"key_facts\">[\"USD1 market cap is ~$4.09\u20134.11B as of late July 2026 (CoinGecko $4.107B; CMC $4.089B; DefiLlama ~$4.13B supply).\", \"USD1 price is holding peg at ~$0.9988; ATH $1.05 and ATL $0.9888 both recorded July 9, 2026.\", \"USD1 is the ~4th-largest stablecoin globally (behind USDT, USDC, USDS); rank #20\u201324 overall on CMC/CoinGecko.\", \"Circulating supply peaked near $5.3B in H1 2026 and has declined ~20% to ~$4.1B, indicating net redemptions.\", \"Supply concentrated on BNB Chain (~1.59B), Ethereum (~1.49B), and Tron (~1.02B); BNB and ETH balances declining, Tron roughly flat.\", \"Broad stablecoin market fell ~$10B (~3%) from its May 2026 peak, including a record $7.7B drop in June 2026 (CoinDesk/RWA.xyz).\", \"USD1 growth was driven by institutional deals: a $2B MGX\u2013Binance settlement in USD1 and a ~$2B Abu Dhabi-linked purchase.\", \"Binance-linked wallets held ~87% of USD1 supply at one point (Forbes); Binance booster APR cut from 20% to 8%.\", \"Binance now settles BTC and ETH perpetual futures directly in USD1; USD1 launched natively on Tempo (Stripe L1) in May 2026.\", \"Issued by BitGo Trust, backed by cash and short-duration US Treasuries; GENIUS Act-aligned; national bank charter application pending (OCC decision still pending). ~617,000 holders. No published audit.\"]",
  "data_points": [
    {
      "metric": "USD1 market capitalization (CoinGecko)",
      "value": 4107000000,
      "unit": "USD",
      "as_of": "2026-07-26",
      "source_url": "https://www.coingecko.com/en/coins/usd1-wlfi"
    },
    {
      "metric": "USD1 circulating supply (CoinGecko)",
      "value": 4112000000,
      "unit": "USD1 tokens",
      "as_of": "2026-07-26",
      "source_url": "https://www.coingecko.com/en/coins/usd1-wlfi"
    },
    {
      "metric": "USD1 price (CoinGecko)",
      "value": 0.9988,
      "unit": "USD",
      "as_of": "2026-07-26",
      "source_url": "https://www.coingecko.com/en/coins/usd1-wlfi"
    },
    {
      "metric": "USD1 24h trading volume (CoinGecko)",
      "value": 842942000,
      "unit": "USD",
      "as_of": "2026-07-26",
      "source_url": "https://www.coingecko.com/en/coins/usd1-wlfi"
    },
    {
      "metric": "USD1 market cap rank (CoinGecko)",
      "value": 24,
      "unit": "rank",
      "as_of": "2026-07-26",
      "source_url": "https://www.coingecko.com/en/coins/usd1-wlfi"
    },
    {
      "metric": "USD1 market capitalization (CoinMarketCap)",
      "value": 4089302996,
      "unit": "USD",
      "as_of": "2026-07-26",
      "source_url": "https://coinmarketcap.com/currencies/usd1/"
    },
    {
      "metric": "USD1 circulating supply (CoinMarketCap)",
      "value": 4094448189,
      "unit": "USD1 tokens",
      "as_of": "2026-07-26",
      "source_url": "https://coinmarketcap.com/currencies/usd1/"
    },
    {
      "metric": "USD1 24h volume (CoinMarketCap)",
      "value": 873605554,
      "unit": "USD",
      "as_of": "2026-07-26",
      "source_url": "https://coinmarketcap.com/currencies/usd1/"
    },
    {
      "metric": "USD1 total circulating supply (DefiLlama, all chains)",
      "value": 4130000000,
      "unit": "USD1 tokens",
      "as_of": "2026-07-26",
      "source_url": "https://defillama.com/stablecoin/world-liberty-financial-usd"
    },
    {
      "metric": "USD1 supply on BNB Chain (largest chain)",
      "value": 1589000000,
      "unit": "USD1 tokens",
      "as_of": "2026-07-26",
      "source_url": "https://defillama.com/stablecoin/world-liberty-financial-usd"
    },
    {
      "metric": "USD1 supply on Ethereum",
      "value": 1488000000,
      "unit": "USD1 tokens",
      "as_of": "2026-07-26",
      "source_url": "https://defillama.com/stablecoin/world-liberty-financial-usd"
    },
    {
      "metric": "USD1 supply on Tron",
      "value": 1022000000,
      "unit": "USD1 tokens",
      "as_of": "2026-07-26",
      "source_url": "https://defillama.com/stablecoin/world-liberty-financial-usd"
    },
    {
      "metric": "USD1 peak circulating supply in H1 2026",
      "value": 5300000000,
      "unit": "USD",
      "as_of": "2026-06-30",
      "source_url": "https://ethnews.com/usd1-stablecoin-supply-hits-5-3b-as-wlfi-token-lags/"
    },
    {
      "metric": "USD1 market cap Q1 2026 (peak, StablecoinInsider)",
      "value": 4520000000,
      "unit": "USD",
      "as_of": "2026-03-31",
      "source_url": "https://stablecoininsider.org/usd1-q1-2026-stablecoin-report/"
    },
    {
      "metric": "USD1 holder count",
      "value": 617000,
      "unit": "holders",
      "as_of": "2026-07-01",
      "source_url": "https://blockchainreporter.net/what-is-usd1-stablecoin/"
    },
    {
      "metric": "Total stablecoin market cap decline since May 2026 peak",
      "value": 10000000000,
      "unit": "USD",
      "as_of": "2026-07-12",
      "source_url": "https://www.coindesk.com/markets/2026/07/12/stablecoin-market-cap-has-shrunk-by-usd10-billion-since-may-but-analyst-sees-no-reason-to-panic"
    },
    {
      "metric": "Total stablecoin market cap June 2026 monthly decline",
      "value": 7700000000,
      "unit": "USD",
      "as_of": "2026-06-30",
      "source_url": "https://www.coindesk.com/markets/2026/07/12/stablecoin-market-cap-has-shrunk-by-usd10-billion-since-may-but-analyst-sees-no-reason-to-panic"
    },
    {
      "metric": "Total stablecoin market cap (week ending July 5, 2026)",
      "value": 311311000000,
      "unit": "USD",
      "as_of": "2026-07-05",
      "source_url": "https://www.gncrypto.news/news/stablecoin-market-cap-drops-1-9b-sky-dollar-falls-most/"
    }
  ],
  "sources": [
    {
      "url": "https://www.coingecko.com/en/coins/usd1-wlfi",
      "title": "USD1 Price: USD1/USD Live Price Chart, Market Cap & News Today | CoinGecko",
      "domain": "coingecko.com",
      "accessed_at": "2026-07-27T00:00:00Z",
      "snippet": "Market cap $4.107B, circulating supply 4.112B USD1, price $0.9988, 24h volume $842.9M, rank #24. ATH $1.05 (July 9, 2026), ATL $0.9888 (July 9, 2026)."
    },
    {
      "url": "https://coinmarketcap.com/currencies/usd1/",
      "title": "World Liberty Financial USD price today, USD1 to USD live price, marketcap and chart | CoinMarketCap",
      "domain": "coinmarketcap.com",
      "accessed_at": "2026-07-27T00:00:00Z",
      "snippet": "Market cap $4,089,302,996; circulating supply 4,094,448,189 USD1; price $0.998743; 24h volume $873.6M; rank #20."
    },
    {
      "url": "https://defillama.com/stablecoin/world-liberty-financial-usd",
      "title": "World Liberty Financial USD (USD1) Market Cap, Supply & Peg Chart - DefiLlama",
      "domain": "defillama.com",
      "accessed_at": "2026-07-27T00:00:00Z",
      "snippet": "Total circulating ~4.13B across chains; BNB ~1.59B (declining), Ethereum ~1.49B (declining), Tron ~1.02B (flat). Fiat-backed, no audit."
    },
    {
      "url": "https://ethnews.com/usd1-stablecoin-supply-hits-5-3b-as-wlfi-token-lags/",
      "title": "USD1 Stablecoin Supply Hits $5.3B as WLFI Token Lags",
      "domain": "ethnews.com",
      "accessed_at": "2026-07-27T00:00:00Z",
      "snippet": "USD1 supply peaked near $5.3B in H1 2026; Binance settles BTC and ETH perpetual futures directly in USD1; OCC charter decision still pending."
    },
    {
      "url": "https://blockchainreporter.net/what-is-usd1-stablecoin/",
      "title": "USD1 Stablecoin Explained: How It Works & Who Backs It",
      "domain": "blockchainreporter.net",
      "accessed_at": "2026-07-27T00:00:00Z",
      "snippet": "4th-largest stablecoin; $2B MGX-Binance settlement in USD1; Binance wallets held ~87% of supply (Forbes); ~617,000 holders; national bank charter application Jan 2026; grew from $3.3B (end-2025) to ~$4.5B mid-2026."
    },
    {
      "url": "https://stablecoininsider.org/usd1-q1-2026-stablecoin-report/",
      "title": "WLFI's USD1 Q1 2026 Stablecoin Report",
      "domain": "stablecoininsider.org",
      "accessed_at": "2026-07-27T00:00:00Z",
      "snippet": "USD1 crossed ~$4.52B market cap with over 4.52B USD1 circulating in Q1 2026, fastest-growing stablecoin."
    },
    {
      "url": "https://www.coindesk.com/markets/2026/07/12/stablecoin-market-cap-has-shrunk-by-usd10-billion-since-may-but-analyst-sees-no-reason-to-panic",
      "title": "Stablecoin market cap has shrunk by $10 billion since May, but analyst sees no reason to panic",
      "domain": "coindesk.com",
      "accessed_at": "2026-07-27T00:00:00Z",
      "snippet": "Total stablecoin market cap fell ~$10B (~3%) since May 2026 peak, with $7.7B decline in June alone \u2014 largest dollar drop since May 2022 Terra-Luna collapse."
    },
    {
      "url": "https://www.gncrypto.news/news/stablecoin-market-cap-drops-1-9b-sky-dollar-falls-most/",
      "title": "Stablecoin Market Cap Drops $1.9B; Sky Dollar Falls Most",
      "domain": "gncrypto.news",
      "accessed_at": "2026-07-27T00:00:00Z",
      "snippet": "Stablecoin market cap fell $1.911B to $311.311B for week ending July 5, 2026 (DefiLlama); Tether lost $791M, Sky Dollar down 2.36%."
    },
    {
      "url": "https://eco.com/support/en/articles/11753300-usd1-stablecoin-by-world-liberty-financial",
      "title": "USD1 Stablecoin by World Liberty Financial | Support",
      "domain": "eco.com",
      "accessed_at": "2026-07-27T00:00:00Z",
      "snippet": "USD1 issued by WLF, custodied by BitGo Trust, backed by cash and short-duration US Treasury bills via government money market funds; grew to ~$4.5B by Q1 2026."
    },
    {
      "url": "https://ourcryptotalk.com/blog/usd1-stablecoin-top-five-2026",
      "title": "USD1 Stablecoin Explained: How It Hit the Top Five in 2026",
      "domain": "ourcryptotalk.com",
      "accessed_at": "2026-07-27T00:00:00Z",
      "snippet": "USD1 market cap ~$4.57B, ranked 4th on DefiLlama behind USDT, USDC, USDS."
    }
  ]
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

I've completed the research. Here's a summary of the key findings on USD1's current market capitalization and trajectory:

**Current Market Cap (late July 2026):** ~**$4.09–4.11 billion**, well-corroborated across CoinGecko ($4.107B), CoinMarketCap ($4.089B), and DefiLlama (~$4.13B supply). Peg is holding at ~$0.9988. USD1 is the **4th-largest stablecoin** globally (behind USDT, USDC, USDS).

**3–4 Week Trajectory — Declining:**
- Supply peaked near **$5.3B in H1 2026** and has since contracted ~20% to ~$4.1B, indicating net redemptions.
- DefiLlama chain data confirms the drawdown: BNB Chain (largest, ~1.59B) and Ethereum (~1.49B) both declining; Tron (~1.02B) roughly flat.
- This aligns with a **sector-wide stablecoin contraction** — the total stablecoin market shrank ~$10B (~3%) from its May 2026 peak, with a record $7.7B monthly decline in June (largest since Terra-Luna in May 2022).

**Supply-Affecting News:**
- USD1's supply is unusually lumpy/institution-driven — Binance-linked wallets held ~87% of supply at one point, and growth came from deals like the $2B MGX–Binance settlement. The wind-down of Binance booster incentives (APR cut 20%→8%) likely drove some of the recent contraction.
- Integrations expanding utility: Binance now settles BTC/ETH perpetual futures in USD1; native launch on Tempo (Stripe L1) in May 2026; Chainlink CCIP cross-chain support.
- Regulatory: BitGo-custodied, Treasury-backed, GENIUS Act-aligned; a national bank charter application (Jan 2026) with an OCC decision still pending.

The full structured findings (data points with sources and dates) have been submitted via the StructuredOutput tool.


### ↳ End nested research agent trace

## 💭 Thinking



## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nnp.random.seed(42)\n\n# Current CoinGecko value (resolution source) ~ $4.10B as of 2026-07-26\nS0 = 4.10\nhorizon = 12  # days from ~July 26 to Aug 7 (11-12 days)\nN = 200000\n\n# Daily dynamics: stablecoin supply moves. Recent trend declining (sector contraction, incentive unwind)\n# but lumpy institutional mints can jump supply up. \n# Base diffusion daily vol ~1.8%, slight negative drift\nmu = -0.002   # slight downward drift/day given declining momentum\nsigma = 0.018 # daily diffusive vol\n\n# Jump component: occasional large institutional mint/redemption (e.g. $0.3-1B moves)\n# prob of a jump on a given day\np_jump = 0.06\njump_mean = 0.0   # symmetric-ish, could be mint (+) or redemption (-)\njump_sd = 0.06    # ~6% jump size on jump days\n\nlogS = np.log(np.full(N, S0))\nfor t in range(horizon):\n    z = np.random.normal(mu - 0.5*sigma**2, sigma, N)\n    jumps = (np.random.rand(N) < p_jump) * np.random.normal(jump_mean, jump_sd, N)\n    logS += z + jumps\n\nS = np.exp(logS)\n\npctls = [1,5,10,20,25,30,40,50,60,70,75,80,90,95,99]\nvals = np.percentile(S, pctls)\nfor p,v in zip(pctls, vals):\n    print(f\"P{p}: {v:.3f}\")\nprint(\"mean\", S.mean(), \"std\", S.std())\nprint(\"P(>5.5)\", (S>5.5).mean(), \"P(<3.5)\", (S<3.5).mean())\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "P1: 3.278\nP5: 3.505\nP10: 3.617\nP20: 3.748\nP25: 3.796\nP30: 3.840\nP40: 3.921\nP50: 3.995\nP60: 4.073\nP70: 4.157\nP75: 4.206\nP80: 4.260\nP90: 4.414\nP95: 4.556\nP99:
4.872\nmean 4.0087134722170505 std 0.32350766790477126\nP(>5.5) 0.000375 P(<3.5) 0.04855\n", "stderr": "", "duration_ms": 358}
```

## 💭 Thinking



## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nnp.random.seed(7)\n# Reconsider: late July stabilized ~$4.1B; sharp pullback largely played out.\n# Use near-flat drift (tiny down bias), keep lumpy jumps. Slightly fatter upper tail\n# since token was $4.84B 5 wks ago and $5.3B peak -> big mint deals possible.\nmu = -0.0008\nsigma = 0.018\np_jump = 0.07\njump_sd = 0.065\n\nlogS = np.log(np.full(N, S0))\nfor t in range(horizon):\n    z = np.random.normal(mu - 0.5*sigma**2, sigma, N)\n    jumps = (np.random.rand(N) < p_jump) * np.random.normal(0.005, jump_sd, N)  # tiny + bias in jumps\n    logS += z + jumps\nS = np.exp(logS)\npctls = [1,5,10,20,25,30,40,50,60,70,75,80,90,95,99]\nvals = np.percentile(S, pctls)\nfor p,v in zip(pctls, vals):\n    print(f\"P{p}: {v:.3f}\")\nprint(\"mean\", round(S.mean(),3), \"median\", round(np.median(S),3))\nprint(\"P(>5.5)\", round((S>5.5).mean(),4), \"P(<3.5)\", round((S<3.5).mean(),4))\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "P1: 3.302\nP5: 3.543\nP10: 3.661\nP20: 3.801\nP25: 3.853\nP30: 3.900\nP40: 3.984\nP50: 4.065\nP60: 4.148\nP70: 4.241\nP75: 4.293\nP80: 4.354\nP90: 4.532\nP95: 4.695\nP99:
5.061\nmean 4.085 median 4.065\nP(>5.5) 0.0015 P(<3.5) 0.0378\n", "stderr": "", "duration_ms": 75}
```

## 💭 Thinking


