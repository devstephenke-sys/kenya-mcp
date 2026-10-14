"""Kenya MCP Server - Main server implementation."""

import json
from typing import Any, Dict, List, Optional

from mcp.server import MCPServer

from kenya_mcp.client import KenyaAPIClient, TreasuryClient, TendersClient


# Initialize MCP server
mcp = MCPServer("kenya-mcp")


@mcp.tool()
async def kenya_search(
    query: str,
    resource_type: Optional[str] = None,
) -> str:
    """Global search across all KenyaAPI resources.

    Search across counties, constituencies, holidays, institutions, ministries,
    and exchange rates in a single request.

    Args:
        query: Search term (minimum 2 characters)
        resource_type: Narrow to one resource type: counties, constituencies,
                      holidays, institutions, ministries, exchange_rates

    Returns:
        JSON string with grouped search results
    """
    async with KenyaAPIClient() as client:
        result = await client.search(query=query, resource_type=resource_type)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_counties(
    name: Optional[str] = None,
    sort: Optional[str] = None,
) -> str:
    """Get county data for all 47 Kenyan counties.

    Args:
        name: Filter by county name (e.g., "Nairobi")
        sort: Sort order (e.g., "name", "id")

    Returns:
        JSON string with county data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_counties(name=name, sort=sort)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_county_details(county_id: int) -> str:
    """Get detailed information about a specific county.

    Args:
        county_id: County ID (1-47)

    Returns:
        JSON string with county details including governor information
    """
    async with KenyaAPIClient() as client:
        result = await client.get_county_details(county_id=county_id)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_constituencies(
    county_id: Optional[int] = None,
    name: Optional[str] = None,
) -> str:
    """Get constituency data.

    Args:
        county_id: Filter by county ID
        name: Filter by constituency name

    Returns:
        JSON string with constituency data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_constituencies(county_id=county_id, name=name)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_public_holidays(
    year: Optional[int] = None,
) -> str:
    """Get Kenyan public holidays.

    Args:
        year: Filter by year (e.g., 2024)

    Returns:
        JSON string with public holiday data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_public_holidays(year=year)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_population(
    county_id: Optional[int] = None,
) -> str:
    """Get population statistics.

    Args:
        county_id: Filter by county ID

    Returns:
        JSON string with population data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_population(county_id=county_id)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_exchange_rates() -> str:
    """Get current exchange rates from Central Bank of Kenya.

    Returns:
        JSON string with exchange rate data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_exchange_rates()
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_educational_institutions(
    institution_type: Optional[str] = None,
    county_id: Optional[int] = None,
) -> str:
    """Get educational institutions (universities, TVETs, polytechnics).

    Args:
        institution_type: Filter by type (universities, tvets, polytechnics)
        county_id: Filter by county ID

    Returns:
        JSON string with educational institution data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_educational_institutions(
            institution_type=institution_type,
            county_id=county_id,
        )
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_universities(
    county_id: Optional[int] = None,
) -> str:
    """Get universities.

    Args:
        county_id: Filter by county ID

    Returns:
        JSON string with university data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_universities(county_id=county_id)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_tvets(
    county_id: Optional[int] = None,
) -> str:
    """Get TVETs and polytechnics.

    Args:
        county_id: Filter by county ID

    Returns:
        JSON string with TVET and polytechnic data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_tvets(county_id=county_id)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_health_facilities(
    county_id: Optional[int] = None,
    facility_type: Optional[str] = None,
) -> str:
    """Get health facilities.

    Args:
        county_id: Filter by county ID
        facility_type: Filter by facility type

    Returns:
        JSON string with health facility data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_health_facilities(
            county_id=county_id,
            facility_type=facility_type,
        )
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_ministries() -> str:
    """Get government ministries.

    Returns:
        JSON string with ministry data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_ministries()
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_parastatals() -> str:
    """Get government parastatals.

    Returns:
        JSON string with parastatal data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_parastatals()
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_presidents() -> str:
    """Get historical presidents data.

    Returns:
        JSON string with presidents data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_presidents()
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_parks_reserves() -> str:
    """Get parks and reserves.

    Returns:
        JSON string with parks and reserves data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_parks_reserves()
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_lakes() -> str:
    """Get lakes data.

    Returns:
        JSON string with lakes data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_lakes()
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_rivers() -> str:
    """Get rivers data.

    Returns:
        JSON string with rivers data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_rivers()
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_postal_codes(
    county_id: Optional[int] = None,
    code: Optional[str] = None,
) -> str:
    """Get postal codes.

    Args:
        county_id: Filter by county ID
        code: Filter by postal code

    Returns:
        JSON string with postal code data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_postal_codes(county_id=county_id, code=code)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_wards(
    county_id: Optional[int] = None,
    constituency_id: Optional[int] = None,
) -> str:
    """Get ward-level data.

    Args:
        county_id: Filter by county ID
        constituency_id: Filter by constituency ID

    Returns:
        JSON string with ward data
    """
    async with KenyaAPIClient() as client:
        result = await client.get_wards(
            county_id=county_id,
            constituency_id=constituency_id,
        )
        return json.dumps(result, indent=2)


# Treasury and Finance Tools


@mcp.tool()
async def kenya_get_budget_books(
    financial_year: Optional[str] = None,
) -> str:
    """Get budget books from Kenya National Treasury.

    Access official budget estimates documents including recurrent and development
    budget books for specified financial years.

    Args:
        financial_year: Filter by financial year (e.g., "2025-2026")

    Returns:
        JSON string with budget books page content and download links
    """
    async with TreasuryClient() as client:
        result = await client.get_budget_books(financial_year=financial_year)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_budget_summary(
    financial_year: Optional[str] = None,
) -> str:
    """Get budget summary documents from Kenya National Treasury.

    Access budget summary and supporting information documents including fiscal
    responsibility statements and medium-term budget information.

    Args:
        financial_year: Filter by financial year (e.g., "2026-2027")

    Returns:
        JSON string with budget summary page content
    """
    async with TreasuryClient() as client:
        result = await client.get_budget_summary(financial_year=financial_year)
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_qebr_report(
    year: Optional[int] = None,
    quarter: Optional[str] = None,
) -> str:
    """Get Quarterly Economic and Budgetary Review (QEBR) reports.

    Access quarterly economic reports with fiscal developments, revenue,
    expenditure, public debt, and economic indicators.

    Args:
        year: Financial year (e.g., 2025)
        quarter: Quarter name (e.g., "First", "Second", "Third", "Fourth")

    Returns:
        JSON string with QEBR report information
    """
    async with TreasuryClient() as client:
        result = await client.get_qebr_report(year=year, quarter=quarter)
        return json.dumps(result, indent=2)


# Tenders and Procurement Tools


@mcp.tool()
async def kenya_search_tenders(
    keyword: Optional[str] = None,
    category: Optional[str] = None,
    county: Optional[str] = None,
) -> str:
    """Search government tenders from tenders.go.ke (official PPRA portal).

    Search for public procurement opportunities including works, goods, services,
    and consultancy tenders from government entities.

    Args:
        keyword: Search keyword (e.g., "ICT", "construction", "medical")
        category: Filter by category (Works, Goods, Services, Consultancy)
        county: Filter by county name (e.g., "Nairobi", "Kisumu")

    Returns:
        JSON string with tender search results (HTML content for parsing)
    """
    async with TendersClient() as client:
        result = await client.search_tenders(
            keyword=keyword,
            category=category,
            county=county,
        )
        return json.dumps(result, indent=2)


@mcp.tool()
async def kenya_get_tender_details(tender_id: str) -> str:
    """Get details for a specific government tender.

    Retrieve full tender details including description, procuring entity,
    closing date, and document links.

    Args:
        tender_id: Tender ID or reference number

    Returns:
        JSON string with tender details (HTML content for parsing)
    """
    async with TendersClient() as client:
        result = await client.get_tender_details(tender_id=tender_id)
        return json.dumps(result, indent=2)


if __name__ == "__main__":
    # Run with: uv run mcp dev kenya_mcp/server.py
    # Or for production: uv run mcp run kenya_mcp/server.py --transport stdio
    pass
