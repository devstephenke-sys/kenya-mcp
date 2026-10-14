# Kenya MCP Server

A Model Context Protocol (MCP) server for accessing public data from Kenya government resources. This server provides tools to query data from KenyaAPI, which aggregates official data from IEBC, KNBS, Central Bank of Kenya, Office of the President, CUE, TVETA, Kenya Wildlife Service, and other government sources. Also includes tools for accessing Treasury budget documents and government tenders.

## Features

- **Administrative Data**: Counties, constituencies, wards, postal codes
- **Government Institutions**: Ministries, parastatals, presidents
- **Health Data**: Health facilities across Kenya
- **Education Data**: Universities, TVETs, polytechnics
- **Economic Data**: Exchange rates from Central Bank of Kenya
- **Demographic Data**: Population statistics
- **Geographical Data**: Parks, reserves, lakes, rivers
- **Public Holidays**: Kenyan public holidays by year
- **Finance & Budget**: Treasury budget books, budget summaries, QEBR reports
- **Tenders & Procurement**: Government tenders from tenders.go.ke
- **Global Search**: Search across all resources simultaneously

## Installation

### Using uv (recommended)

```bash
cd kenya-mcp
uv install
```

### Using pip

```bash
cd kenya-mcp
pip install -e .
```

## Configuration

No API keys or authentication required! KenyaAPI is publicly accessible.

To use this MCP server with Devin, add it to your MCP configuration file:

```json
{
  "mcpServers": {
    "kenya-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "path/to/kenya-mcp",
        "run",
        "mcp",
        "run",
        "server.py",
        "--transport",
        "stdio"
      ]
    }
  }
}
```

Replace `path/to/kenya-mcp` with the actual path to the kenya-mcp directory.

## Available Tools

### Search & Discovery

- `kenya_search` - Global search across all resources
- `kenya_get_counties` - Get all 47 counties
- `kenya_get_county_details` - Get specific county details including governor
- `kenya_get_constituencies` - Get constituency data
- `kenya_get_wards` - Get ward-level data
- `kenya_get_postal_codes` - Get postal codes

### Government & Administrative

- `kenya_get_ministries` - Get government ministries
- `kenya_get_parastatals` - Get government parastatals
- `kenya_get_presidents` - Get historical presidents data

### Health & Education

- `kenya_get_health_facilities` - Get health facilities
- `kenya_get_universities` - Get universities
- `kenya_get_tvets` - Get TVETs and polytechnics
- `kenya_get_educational_institutions` - Get all educational institutions

### Economic & Demographic

- `kenya_get_exchange_rates` - Get current exchange rates from Central Bank
- `kenya_get_population` - Get population statistics

### Geographical

- `kenya_get_parks_reserves` - Get parks and reserves
- `kenya_get_lakes` - Get lakes data
- `kenya_get_rivers` - Get rivers data

### Other

- `kenya_get_public_holidays` - Get public holidays by year

### Finance & Budget

- `kenya_get_budget_books` - Get budget books from National Treasury (recurrent & development estimates)
- `kenya_get_budget_summary` - Get budget summary documents and fiscal information
- `kenya_get_qebr_report` - Get Quarterly Economic and Budgetary Review reports

### Tenders & Procurement

- `kenya_search_tenders` - Search government tenders from tenders.go.ke (PPRA portal)
- `kenya_get_tender_details` - Get details for a specific tender

## Usage Examples

### Search for data

```python
# Search for "Nairobi" across all resources
result = await kenya_search(query="Nairobi")

# Search for holidays specifically
result = await kenya_search(query="holiday", resource_type="holidays")
```

### Get county data

```python
# Get all counties
result = await kenya_get_counties()

# Get specific county details
result = await kenya_get_county_details(county_id=47)  # Nairobi

# Filter counties by name
result = await kenya_get_counties(name="Nairobi")
```

### Get health facilities

```python
# Get all health facilities
result = await kenya_get_health_facilities()

# Filter by county
result = await kenya_get_health_facilities(county_id=47)
```

### Get exchange rates

```python
# Get current exchange rates from Central Bank of Kenya
result = await kenya_get_exchange_rates()
```

### Get public holidays

```python
# Get all holidays
result = await kenya_get_public_holidays()

# Get holidays for a specific year
result = await kenya_get_public_holidays(year=2024)
```

### Get Treasury budget documents

```python
# Get budget books page
result = await kenya_get_budget_books()

# Get budget books for specific financial year
result = await kenya_get_budget_books(financial_year="2025-2026")

# Get budget summary
result = await kenya_get_budget_summary(financial_year="2026-2027")

# Get QEBR report
result = await kenya_get_qebr_report(year=2025, quarter="Fourth")
```

### Search government tenders

```python
# Search all tenders
result = await kenya_search_tenders()

# Search with keyword
result = await kenya_search_tenders(keyword="ICT")

# Filter by category and county
result = await kenya_search_tenders(
    keyword="construction",
    category="Works",
    county="Nairobi"
)

# Get specific tender details
result = await kenya_get_tender_details(tender_id="PPRA/2026/001")
```

## Data Sources

### Primary: KenyaAPI

- **URL**: https://kenya-api.netlify.app
- **Description**: Aggregates public data from multiple Kenya government sources
- **Rate Limit**: 100 requests per minute per IP
- **Authentication**: None required
- **Data Sources**:
  - IEBC (Independent Electoral and Boundaries Commission)
  - KNBS (Kenya National Bureau of Statistics)
  - Central Bank of Kenya
  - Office of the President
  - CUE (Commission for University Education)
  - TVETA (Technical and Vocational Education and Training Authority)
  - Kenya Wildlife Service
  - Other official government sources

### Secondary: KNBS National Statistical Repository

- **URL**: https://repository.knbs.or.ke
- **Description**: Official statistics, surveys, census data
- **Access**: Some datasets require formal requests per data access policy
- **Status**: Not yet integrated (planned for future enhancement)

### Treasury & Finance

- **URL**: https://treasury.go.ke
- **Description**: National Treasury budget books, budget summaries, and QEBR reports
- **Access**: Public documents (PDF format)
- **Data Available**:
  - Budget Books (Recurrent & Development estimates)
  - Budget Summary documents
  - Quarterly Economic and Budgetary Review (QEBR) reports
  - Financial statements
- **Note**: Data is fetched as HTML/links - requires PDF parsing for structured data

### Tenders & Procurement

- **URL**: https://tenders.go.ke
- **Description**: Official government procurement portal managed by PPRA
- **Access**: Public web portal
- **Data Available**:
  - Government tenders (Works, Goods, Services, Consultancy)
  - Tender details, closing dates, procuring entities
  - County-specific tenders
- **Note**: Data is fetched as HTML - requires parsing for structured data
- **Alternative**: Tendersoko Africa API (https://api.tendersoko.africa) - Professional API with structured JSON (~$405/month, requires API key)

### Government Projects

- **GPRIS**: https://gpris.go.ke - Government Project Reporting Information System (real-time project data, budgets, progress)
- **NGDS**: https://ngds.primecs.go.ke - National Government Dashboard System (51+ tracked projects)
- **County PMTS**: County-specific project monitoring systems (some have REST APIs)
- **Note**: Most project portals are web dashboards without public API access - web scraping would be required

## Rate Limiting

KenyaAPI enforces a rate limit of 100 requests per minute per IP address. If you exceed this limit, you will receive a 429 HTTP status code. The client will automatically raise an error in this case.

## Development

### Running locally for testing

```bash
cd kenya-mcp
uv run mcp dev server.py
```

### Building for production

```bash
cd kenya-mcp
uv build
```

## License

MIT License

## Data Licensing

The data provided through this MCP server comes from various Kenya government sources, each with their own licensing terms. KenyaAPI aggregates data from sources that are publicly available under open licenses. Please refer to the specific data source for detailed licensing information:

- **KenyaAPI**: Aggregates data from multiple official sources
- **KNBS**: Official statistics - may have specific usage requirements
- **IEBC**: Electoral data - public domain
- **Central Bank of Kenya**: Financial data - public domain

Always attribute data to its original source when using it in publications or applications.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Support

For issues specific to this MCP server, please open an issue on the repository.

For issues with the underlying data:
- KenyaAPI: https://kenya-api.netlify.app/docs.html
- KNBS: https://www.knbs.or.ke
