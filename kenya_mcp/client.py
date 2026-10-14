"""Kenya API Client for interacting with Kenya government public data."""

import httpx
from typing import Any, Dict, List, Optional


class KenyaAPIClient:
    """Client for the KenyaAPI public data service."""

    BASE_URL = "https://kenya-api.netlify.app/api/v1"

    def __init__(self):
        """Initialize KenyaAPI client.

        Note: No authentication required for KenyaAPI.
        """
        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        """Async context manager entry."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        self._client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers=headers,
            timeout=60.0,
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self._client:
            await self._client.aclose()

    async def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make an HTTP request to the KenyaAPI.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Query parameters

        Returns:
            Response data as dictionary
        """
        if not self._client:
            raise RuntimeError("Client not initialized. Use async context manager.")

        response = await self._client.request(
            method=method,
            url=endpoint,
            params=params,
        )
        response.raise_for_status()
        return response.json()

    async def search(
        self,
        query: str,
        resource_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Global search across all KenyaAPI resources.

        Args:
            query: Search term (min 2 characters)
            resource_type: Narrow to one resource type (counties, constituencies,
                          holidays, institutions, ministries, exchange_rates)

        Returns:
            Search results with grouped data by resource type
        """
        params = {"q": query}
        if resource_type:
            params["type"] = resource_type

        return await self._request("GET", "/search", params=params)

    async def get_counties(
        self,
        name: Optional[str] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get county data for all 47 Kenyan counties.

        Args:
            name: Filter by county name
            sort: Sort order (e.g., "name", "id")

        Returns:
            County data
        """
        params = {}
        if name:
            params["name"] = name
        if sort:
            params["sort"] = sort

        return await self._request("GET", "/counties", params=params)

    async def get_county_details(self, county_id: int) -> Dict[str, Any]:
        """Get detailed information about a specific county.

        Args:
            county_id: County ID (1-47)

        Returns:
            County details including governor information
        """
        return await self._request("GET", f"/counties/{county_id}")

    async def get_constituencies(
        self,
        county_id: Optional[int] = None,
        name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get constituency data.

        Args:
            county_id: Filter by county ID
            name: Filter by constituency name

        Returns:
            Constituency data
        """
        params = {}
        if county_id:
            params["county_id"] = county_id
        if name:
            params["name"] = name

        return await self._request("GET", "/constituencies", params=params)

    async def get_public_holidays(
        self,
        year: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get Kenyan public holidays.

        Args:
            year: Filter by year (e.g., 2024)

        Returns:
            Public holiday data
        """
        params = {}
        if year:
            params["year"] = year

        return await self._request("GET", "/holidays", params=params)

    async def get_population(
        self,
        county_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get population statistics.

        Args:
            county_id: Filter by county ID

        Returns:
            Population data
        """
        params = {}
        if county_id:
            params["county_id"] = county_id

        return await self._request("GET", "/population", params=params)

    async def get_exchange_rates(self) -> Dict[str, Any]:
        """Get current exchange rates from Central Bank of Kenya.

        Returns:
            Exchange rate data
        """
        return await self._request("GET", "/exchange-rates")

    async def get_educational_institutions(
        self,
        institution_type: Optional[str] = None,
        county_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get educational institutions (universities, TVETs, polytechnics).

        Args:
            institution_type: Filter by type (universities, tvets, polytechnics)
            county_id: Filter by county ID

        Returns:
            Educational institution data
        """
        params = {}
        if institution_type:
            params["type"] = institution_type
        if county_id:
            params["county_id"] = county_id

        return await self._request("GET", "/institutions", params=params)

    async def get_universities(
        self,
        county_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get universities.

        Args:
            county_id: Filter by county ID

        Returns:
            University data
        """
        params = {}
        if county_id:
            params["county_id"] = county_id

        return await self._request("GET", "/universities", params=params)

    async def get_tvets(
        self,
        county_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get TVETs and polytechnics.

        Args:
            county_id: Filter by county ID

        Returns:
            TVET and polytechnic data
        """
        params = {}
        if county_id:
            params["county_id"] = county_id

        return await self._request("GET", "/tvets", params=params)

    async def get_health_facilities(
        self,
        county_id: Optional[int] = None,
        facility_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get health facilities.

        Args:
            county_id: Filter by county ID
            facility_type: Filter by facility type

        Returns:
            Health facility data
        """
        params = {}
        if county_id:
            params["county_id"] = county_id
        if facility_type:
            params["type"] = facility_type

        return await self._request("GET", "/health-facilities", params=params)

    async def get_ministries(self) -> Dict[str, Any]:
        """Get government ministries.

        Returns:
            Ministry data
        """
        return await self._request("GET", "/ministries")

    async def get_parastatals(self) -> Dict[str, Any]:
        """Get government parastatals.

        Returns:
            Parastatal data
        """
        return await self._request("GET", "/parastatals")

    async def get_presidents(self) -> Dict[str, Any]:
        """Get historical presidents data.

        Returns:
            Presidents data
        """
        return await self._request("GET", "/presidents")

    async def get_parks_reserves(self) -> Dict[str, Any]:
        """Get parks and reserves.

        Returns:
            Parks and reserves data
        """
        return await self._request("GET", "/parks-reserves")

    async def get_lakes(self) -> Dict[str, Any]:
        """Get lakes data.

        Returns:
            Lakes data
        """
        return await self._request("GET", "/lakes")

    async def get_rivers(self) -> Dict[str, Any]:
        """Get rivers data.

        Returns:
            Rivers data
        """
        return await self._request("GET", "/rivers")

    async def get_postal_codes(
        self,
        county_id: Optional[int] = None,
        code: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get postal codes.

        Args:
            county_id: Filter by county ID
            code: Filter by postal code

        Returns:
            Postal code data
        """
        params = {}
        if county_id:
            params["county_id"] = county_id
        if code:
            params["code"] = code

        return await self._request("GET", "/postal-codes", params=params)

    async def get_wards(
        self,
        county_id: Optional[int] = None,
        constituency_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Get ward-level data.

        Args:
            county_id: Filter by county ID
            constituency_id: Filter by constituency ID

        Returns:
            Ward data
        """
        params = {}
        if county_id:
            params["county_id"] = county_id
        if constituency_id:
            params["constituency_id"] = constituency_id

        return await self._request("GET", "/wards", params=params)


class TreasuryClient:
    """Client for Kenya National Treasury documents."""

    BASE_URL = "https://treasury.go.ke"

    def __init__(self):
        """Initialize Treasury client."""
        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        """Async context manager entry."""
        headers = {
            "User-Agent": "Kenya-MCP/1.0.0",
        }

        self._client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers=headers,
            timeout=60.0,
            follow_redirects=True,
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self._client:
            await self._client.aclose()

    async def get_budget_books(
        self,
        financial_year: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get budget books information from Treasury.

        Args:
            financial_year: Filter by financial year (e.g., "2025-2026")

        Returns:
            Budget books information with download links
        """
        if not self._client:
            raise RuntimeError("Client not initialized. Use async context manager.")

        # Treasury budget books page
        url = "/index.php/budget-books"
        response = await self._client.get(url)
        response.raise_for_status()

        # Return the HTML content for parsing
        return {
            "url": f"{self.BASE_URL}{url}",
            "content": response.text,
            "message": "Budget books page fetched. Parsing HTML required to extract specific documents.",
        }

    async def get_budget_summary(
        self,
        financial_year: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get budget summary documents.

        Args:
            financial_year: Filter by financial year (e.g., "2026-2027")

        Returns:
            Budget summary document information
        """
        if not self._client:
            raise RuntimeError("Client not initialized. Use async context manager.")

        # Budget summary page
        url = "/index.php/budget-summary"
        response = await self._client.get(url)
        response.raise_for_status()

        return {
            "url": f"{self.BASE_URL}{url}",
            "content": response.text,
            "message": "Budget summary page fetched. Parsing HTML required to extract specific documents.",
        }

    async def get_qebr_report(
        self,
        year: Optional[int] = None,
        quarter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get Quarterly Economic and Budgetary Review reports.

        Args:
            year: Financial year (e.g., 2025)
            quarter: Quarter (e.g., "First", "Second", "Third", "Fourth")

        Returns:
            QEBR report information
        """
        if not self._client:
            raise RuntimeError("Client not initialized. Use async context manager.")

        # QEBR reports are typically in PDF format
        # We'll return information about available reports
        return {
            "url": f"{self.BASE_URL}/index.php/economic-reports",
            "message": "QEBR reports are available as PDFs. Direct download requires parsing the reports page.",
            "note": "Reports are typically named: 'Quarter X QEBR Report FY YYYY-YY.pdf'",
        }


class TendersClient:
    """Client for Kenya government tenders (web scraping approach)."""

    BASE_URL = "https://tenders.go.ke"

    def __init__(self):
        """Initialize Tenders client."""
        self._client: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        """Async context manager entry."""
        headers = {
            "User-Agent": "Kenya-MCP/1.0.0",
        }

        self._client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            headers=headers,
            timeout=60.0,
            follow_redirects=True,
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self._client:
            await self._client.aclose()

    async def search_tenders(
        self,
        keyword: Optional[str] = None,
        category: Optional[str] = None,
        county: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Search government tenders from tenders.go.ke.

        Args:
            keyword: Search keyword (e.g., "ICT", "construction")
            category: Filter by category (Works, Goods, Services, Consultancy)
            county: Filter by county name

        Returns:
            Tender search results (HTML content for parsing)
        """
        if not self._client:
            raise RuntimeError("Client not initialized. Use async context manager.")

        # Build search URL with query parameters
        params = {}
        if keyword:
            params["search"] = keyword
        if category:
            params["category"] = category
        if county:
            params["county"] = county

        response = await self._client.get("/", params=params)
        response.raise_for_status()

        return {
            "url": str(response.url),
            "content": response.text,
            "message": "Tenders page fetched. HTML parsing required to extract tender details.",
            "filters_applied": {
                "keyword": keyword,
                "category": category,
                "county": county,
            },
        }

    async def get_tender_details(self, tender_id: str) -> Dict[str, Any]:
        """Get details for a specific tender.

        Args:
            tender_id: Tender ID or reference number

        Returns:
            Tender details (HTML content for parsing)
        """
        if not self._client:
            raise RuntimeError("Client not initialized. Use async context manager.")

        response = await self._client.get(f"/tenders/detail/{tender_id}")
        response.raise_for_status()

        return {
            "url": str(response.url),
            "content": response.text,
            "message": "Tender details page fetched. HTML parsing required to extract specific fields.",
        }
