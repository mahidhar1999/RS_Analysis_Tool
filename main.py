import yfinance as yf
from fastapi import FastAPI
from datetime import datetime, timedelta
import pandas as pd
import json
from datetime import datetime
import pytz

stock_symbols = [
    "360ONE",
    "3MINDIA",
    "ABB",
    "ACC",
    "ACMESOLAR",
    "AIAENG",
    "APLAPOLLO",
    "AUBANK",
    "AWL",
    "AADHARHFC",
    "AARTIIND",
    "AAVAS",
    "ABBOTINDIA",
    "ACE",
    "ADANIENSOL",
    "ADANIENT",
    "ADANIGREEN",
    "ADANIPORTS",
    "ADANIPOWER",
    "ATGL",
    "ABCAPITAL",
    "ABFRL",
    "ABREL",
    "ABSLAMC",
    "AEGISLOG",
    "AFCONS",
    "AFFLE",
    "AJANTPHARM",
    "AKUMS",
    "APLLTD",
    "ALIVUS",
    "ALKEM",
    "ALKYLAMINE",
    "ALOKINDS",
    "ARE&M",
    "AMBER",
    "AMBUJACEM",
    "ANANDRATHI",
    "ANANTRAJ",
    "ANGELONE",
    "APARINDS",
    "APOLLOHOSP",
    "APOLLOTYRE",
    "APTUS",
    "ASAHIINDIA",
    "ASHOKLEY",
    "ASIANPAINT",
    "ASTERDM",
    "ASTRAZEN",
    "ASTRAL",
    "ATUL",
    "AUROPHARMA",
    "AIIL",
    "DMART",
    "AXISBANK",
    "BASF",
    "BEML",
    "BLS",
    "BSE",
    "BAJAJ-AUTO",
    "BAJFINANCE",
    "BAJAJFINSV",
    "BAJAJHLDNG",
    "BAJAJHFL",
    "BALKRISIND",
    "BALRAMCHIN",
    "BANDHANBNK",
    "BANKBARODA",
    "BANKINDIA",
    "MAHABANK",
    "BATAINDIA",
    "BAYERCROP",
    "BERGEPAINT",
    "BDL",
    "BEL",
    "BHARATFORG",
    "BHEL",
    "BPCL",
    "BHARTIARTL",
    "BHARTIHEXA",
    "BIKAJI",
    "BIOCON",
    "BSOFT",
    "BLUEDART",
    "BLUESTARCO",
    "BBTC",
    "BOSCHLTD",
    "FIRSTCRY",
    "BRIGADE",
    "BRITANNIA",
    "MAPMYINDIA",
    "CCL",
    "CESC",
    "CGPOWER",
    "CRISIL",
    "CAMPUS",
    "CANFINHOME",
    "CANBK",
    "CAPLIPOINT",
    "CGCL",
    "CARBORUNIV",
    "CASTROLIND",
    "CEATLTD",
    "CENTRALBK",
    "CDSL",
    "CENTURYPLY",
    "CERA",
    "CHALET",
    "CHAMBLFERT",
    "CHENNPETRO",
    "CHOLAHLDNG",
    "CHOLAFIN",
    "CIPLA",
    "CUB",
    "CLEAN",
    "COALINDIA",
    "COCHINSHIP",
    "COFORGE",
    "COLPAL",
    "CAMS",
    "CONCORDBIO",
    "CONCOR",
    "COROMANDEL",
    "CRAFTSMAN",
    "CREDITACC",
    "CROMPTON",
    "CUMMINSIND",
    "CYIENT",
    "DCMSHRIRAM",
    "DLF",
    "DOMS",
    "DABUR",
    "DALBHARAT",
    "DATAPATTNS",
    "DEEPAKFERT",
    "DEEPAKNTR",
    "DELHIVERY",
    "DEVYANI",
    "DIVISLAB",
    "DIXON",
    "LALPATHLAB",
    "DRREDDY",
    "DUMMYSIEMS",
    "EIDPARRY",
    "EIHOTEL",
    "EICHERMOT",
    "ELECON",
    "ELGIEQUIP",
    "EMAMILTD",
    "EMCURE",
    "ENDURANCE",
    "ENGINERSIN",
    "ERIS",
    "ESCORTS",
    "ETERNAL",
    "EXIDEIND",
    "NYKAA",
    "FEDERALBNK",
    "FACT",
    "FINCABLES",
    "FINPIPE",
    "FSL",
    "FIVESTAR",
    "FORTIS",
    "GAIL",
    "GVT&D",
    "GMRAIRPORT",
    "GRSE",
    "GICRE",
    "GILLETTE",
    "GLAND",
    "GLAXO",
    "GLENMARK",
    "MEDANTA",
    "GODIGIT",
    "GPIL",
    "GODFRYPHLP",
    "GODREJAGRO",
    "GODREJCP",
    "GODREJIND",
    "GODREJPROP",
    "GRANULES",
    "GRAPHITE",
    "GRASIM",
    "GRAVITA",
    "GESHIP",
    "FLUOROCHEM",
    "GUJGASLTD",
    "GMDCLTD",
    "GNFC",
    "GPPL",
    "GSPL",
    "HEG",
    "HBLENGINE",
    "HCLTECH",
    "HDFCAMC",
    "HDFCBANK",
    "HDFCLIFE",
    "HFCL",
    "HAPPSTMNDS",
    "HAVELLS",
    "HEROMOTOCO",
    "HSCL",
    "HINDALCO",
    "HAL",
    "HINDCOPPER",
    "HINDPETRO",
    "HINDUNILVR",
    "HINDZINC",
    "POWERINDIA",
    "HOMEFIRST",
    "HONASA",
    "HONAUT",
    "HUDCO",
    "HYUNDAI",
    "ICICIBANK",
    "ICICIGI",
    "ICICIPRULI",
    "IDBI",
    "IDFCFIRSTB",
    "IFCI",
    "IIFL",
    "INOXINDIA",
    "IRB",
    "IRCON",
    "ITC",
    "ITI",
    "INDGN",
    "INDIACEM",
    "INDIAMART",
    "INDIANB",
    "IEX",
    "INDHOTEL",
    "IOC",
    "IOB",
    "IRCTC",
    "IRFC",
    "IREDA",
    "IGL",
    "INDUSTOWER",
    "INDUSINDBK",
    "NAUKRI",
    "INFY",
    "INOXWIND",
    "INTELLECT",
    "INDIGO",
    "IGIL",
    "IKS",
    "IPCALAB",
    "JBCHEPHARM",
    "JKCEMENT",
    "JBMA",
    "JKTYRE",
    "JMFINANCIL",
    "JSWENERGY",
    "JSWHL",
    "JSWINFRA",
    "JSWSTEEL",
    "JPPOWER",
    "J&KBANK",
    "JINDALSAW",
    "JSL",
    "JINDALSTEL",
    "JIOFIN",
    "JUBLFOOD",
    "JUBLINGREA",
    "JUBLPHARMA",
    "JWL",
    "JUSTDIAL",
    "JYOTHYLAB",
    "JYOTICNC",
    "KPRMILL",
    "KEI",
    "KNRCON",
    "KPITTECH",
    "KAJARIACER",
    "KPIL",
    "KALYANKJIL",
    "KANSAINER",
    "KARURVYSYA",
    "KAYNES",
    "KEC",
    "KFINTECH",
    "KIRLOSBROS",
    "KIRLOSENG",
    "KOTAKBANK",
    "KIMS",
    "LTF",
    "LTTS",
    "LICHSGFIN",
    "LTFOODS",
    "LTIM",
    "LT",
    "LATENTVIEW",
    "LAURUSLABS",
    "LEMONTREE",
    "LICI",
    "LINDEINDIA",
    "LLOYDSME",
    "LUPIN",
    "MMTC",
    "MRF",
    "LODHA",
    "MGL",
    "MAHSEAMLES",
    "M&MFIN",
    "M&M",
    "MANAPPURAM",
    "MRPL",
    "MANKIND",
    "MARICO",
    "MARUTI",
    "MASTEK",
    "MFSL",
    "MAXHEALTH",
    "MAZDOCK",
    "METROPOLIS",
    "MINDACORP",
    "MSUMI",
    "MOTILALOFS",
    "MPHASIS",
    "MCX",
    "MUTHOOTFIN",
    "NATCOPHARM",
    "NBCC",
    "NCC",
    "NHPC",
    "NLCINDIA",
    "NMDC",
    "NSLNISP",
    "NTPCGREEN",
    "NTPC",
    "NH",
    "NATIONALUM",
    "NAVA",
    "NAVINFLUOR",
    "NESTLEIND",
    "NETWEB",
    "NETWORK18",
    "NEULANDLAB",
    "NEWGEN",
    "NAM-INDIA",
    "NIVABUPA",
    "NUVAMA",
    "OBEROIRLTY",
    "ONGC",
    "OIL",
    "OLAELEC",
    "OLECTRA",
    "PAYTM",
    "OFSS",
    "POLICYBZR",
    "PCBL",
    "PGEL",
    "PIIND",
    "PNBHOUSING",
    "PNCINFRA",
    "PTCIL",
    "PVRINOX",
    "PAGEIND",
    "PATANJALI",
    "PERSISTENT",
    "PETRONET",
    "PFIZER",
    "PHOENIXLTD",
    "PIDILITIND",
    "PEL",
    "PPLPHARMA",
    "POLYMED",
    "POLYCAB",
    "POONAWALLA",
    "PFC",
    "POWERGRID",
    "PRAJIND",
    "PREMIERENE",
    "PRESTIGE",
    "PNB",
    "RRKABEL",
    "RBLBANK",
    "RECLTD",
    "RHIM",
    "RITES",
    "RADICO",
    "RVNL",
    "RAILTEL",
    "RAINBOW",
    "RKFORGE",
    "RCF",
    "RTNINDIA",
    "RAYMONDLSL",
    "RAYMOND",
    "REDINGTON",
    "RELIANCE",
    "RPOWER",
    "ROUTE",
    "SBFC",
    "SBICARD",
    "SBILIFE",
    "SJVN",
    "SKFINDIA",
    "SRF",
    "SAGILITY",
    "SAILIFE",
    "SAMMAANCAP",
    "MOTHERSON",
    "SAPPHIRE",
    "SARDAEN",
    "SAREGAMA",
    "SCHAEFFLER",
    "SCHNEIDER",
    "SCI",
    "SHREECEM",
    "RENUKA",
    "SHRIRAMFIN",
    "SHYAMMETL",
    "SIEMENS",
    "SIGNATURE",
    "SOBHA",
    "SOLARINDS",
    "SONACOMS",
    "SONATSOFTW",
    "STARHEALTH",
    "SBIN",
    "SAIL",
    "SWSOLAR",
    "SUMICHEM",
    "SUNPHARMA",
    "SUNTV",
    "SUNDARMFIN",
    "SUNDRMFAST",
    "SUPREMEIND",
    "SUVENPHAR",
    "SUZLON",
    "SWANENERGY",
    "SWIGGY",
    "SYNGENE",
    "SYRMA",
    "TBOTEK",
    "TVSMOTOR",
    "TANLA",
    "TATACHEM",
    "TATACOMM",
    "TCS",
    "TATACONSUM",
    "TATAELXSI",
    "TATAINVEST",
    "TATAMOTORS",
    "TATAPOWER",
    "TATASTEEL",
    "TATATECH",
    "TTML",
    "TECHM",
    "TECHNOE",
    "TEJASNET",
    "NIACL",
    "RAMCOCEM",
    "THERMAX",
    "TIMKEN",
    "TITAGARH",
    "TITAN",
    "TORNTPHARM",
    "TORNTPOWER",
    "TARIL",
    "TRENT",
    "TRIDENT",
    "TRIVENI",
    "TRITURBINE",
    "TIINDIA",
    "UCOBANK",
    "UNOMINDA",
    "UPL",
    "UTIAMC",
    "ULTRACEMCO",
    "UNIONBANK",
    "UBL",
    "UNITDSPR",
    "USHAMART",
    "VGUARD",
    "DBREALTY",
    "VTL",
    "VBL",
    "MANYAVAR",
    "VEDL",
    "VIJAYA",
    "VMM",
    "IDEA",
    "VOLTAS",
    "WAAREEENER",
    "WELCORP",
    "WELSPUNLIV",
    "WESTLIFE",
    "WHIRLPOOL",
    "WIPRO",
    "WOCKPHARMA",
    "YESBANK",
    "ZFCVINDIA",
    "ZEEL",
    "ZENTEC",
    "ZENSARTECH",
    "ZYDUSLIFE",
    "ECLERX"
]

nifty_500 = [symbol + ".NS" for symbol in stock_symbols]
#nifty_500 = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]

sector_indices = {
        "NIFTY AUTO": "^CNXAUTO",
        "NIFTY BANK": "^NSEBANK",
        "NIFTY FMCG": "^CNXFMCG",
        "NIFTY IT": "^CNXIT",
        "NIFTY MEDIA": "^CNXMEDIA",
        "NIFTY METAL": "^CNXMETAL",
        "NIFTY PHARMA": "^CNXPHARMA",
        "NIFTY PSU BANK": "^CNXPSUBANK",
        "NIFTY REALTY": "^CNXREALTY",
        "NIFTY ENERGY": "^CNXENERGY",
        "NIFTY INFRA": "^CNXINFRA",
        "NIFTY CONSUMPTION": "^CNXCONSUM",
        "NIFTY MNC": "^CNXMNC",
        "NIFTY PSE": "^CNXPSE",
        "NIFTY SERVICES SECTOR": "^CNXSERVICE",
    }


app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to the RS Screener API 🚀"}

def calculate_pct_change(symbol: str, period: int = 55):
    end_date = datetime.today()
    start_date = end_date - timedelta(days=period * 2)  # Extended range to cover weekends/holidays

    try:
        print(f"\nFetching data for {symbol}")
        print(f"Start Date: {start_date.strftime('%Y-%m-%d')}")
        print(f"End Date: {end_date.strftime('%Y-%m-%d')}")
        
        data = yf.download(symbol, start=start_date, end=end_date)
        
        # Extract 'Close' column as a Series, not DataFrame
        close = data['Close'].squeeze()  # .squeeze() converts a DataFrame to a Series if only one column
        
        print(f"Total data points fetched: {len(close)}")
        
        # Debug: Check the type of 'Close' data
        print(f"Type of 'Close' data: {type(close)}")

        # Drop any rows with NaN values in 'Close' column
        close = close.dropna()
        print(f"Data after dropping NaN values: {len(close)}")

        # Debug: Print out the raw 'Close' data
        print("Raw 'Close' data:")
        print(close.head(10))  # Print first 10 rows to inspect the data
        
        # Ensure that the data is numeric (coerce non-numeric values to NaN)
        close = pd.to_numeric(close, errors='coerce')
        
        # Drop any new NaN values after coercion
        close = close.dropna()

        # Check if there's enough data after cleaning
        if len(close) < period:
            print(f"Not enough trading days for {symbol}. Needed: {period}, Got: {len(close)}")
            return None
        
        # Check the type of the 'Close' column
        print(f"Data type of 'Close' column: {close.dtype}")

        # Take only the last `period` trading days
        close = close.tail(period)
        print(f"Using last {len(close)} trading days for calculation.")
        print("Dates used:")
        print(close.index)

        # Ensure that the first and last values are numeric
        start_price = close.iloc[0]
        end_price = close.iloc[-1]

        # Calculate percentage change using the correct values
        pct_change = (end_price - start_price) / start_price * 100  # Percent change in percentage form
        print(f"Percentage change over {period} trading days: {pct_change:.4f}%")
        return pct_change
    
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None
    
def calculate_rs(stock_symbol: str, comparative_symbol: str = "^NSEI", period: int = 55):
    end_date = datetime.today()
    start_date = end_date - timedelta(days=period * 2)

    try:
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        index_data = yf.download(comparative_symbol, start=start_date, end=end_date)

        if stock_data.empty or index_data.empty:
            print(f"[{stock_symbol}] Data not available.")
            return None

        stock_close = stock_data['Close'].dropna()[-period:]
        index_close = index_data['Close'].dropna()[-period:]

        if len(stock_close) < period or len(index_close) < period:
            print(f"[{stock_symbol}] Not enough trading data.")
            return None

        stock_start = stock_close.iloc[0].item()
        stock_end = stock_close.iloc[-1].item()
        index_start = index_close.iloc[0].item()
        index_end = index_close.iloc[-1].item()


        stock_pct_change = (stock_end - stock_start) / stock_start
        index_pct_change = (index_end - index_start) / index_start

        if index_pct_change == 0:
            return None

        rs = stock_pct_change / index_pct_change
        return rs

    except Exception as e:
        print(f"Error processing {stock_symbol}: {e}")
        return None

    
@app.api_route("/top-stocks", methods=["GET", "HEAD"])
def top_stocks():
    rs_values = []

    # Get the NIFTY market return to determine if it's a bull or bear market
    nifty_return = calculate_pct_change("^NSEI")
    print("nifty_return", nifty_return)

    for stock_symbol in nifty_500:
        rs = calculate_rs(stock_symbol)
        print(stock_symbol, " RS: ", rs)

        try:
            # Fetch 1 year of daily data to calculate 52-week high/low and latest price
            stock_data = yf.download(stock_symbol, period="1y", interval="1d")
            last_traded_price = stock_data['Close'].iloc[-1].item()
            high_52_week = stock_data['High'].max().item()
            low_52_week = stock_data['Low'].min().item()

        except Exception as e:
            print(f"Error fetching data for {stock_symbol}: {e}")
            last_traded_price = None
            high_52_week = None
            low_52_week = None

        if rs is not None and last_traded_price is not None:
            stock_info = {
                "stock_symbol": stock_symbol,
                "relative_strength": rs if nifty_return > 0 else (-1 * rs),
                "last_traded_price": last_traded_price,
                "52_week_high": high_52_week,
                "52_week_low": low_52_week
            }

            # Bull Market: RS > 1
            if nifty_return > 0 and rs > 1:
                rs_values.append(stock_info)
                print(f"Appended {stock_symbol} [Bull] with RS: {rs}, LTP: {last_traded_price}")
            # Bear Market: RS < 1 (falling less)
            elif nifty_return < 0 and rs < 1:
                rs_values.append(stock_info)
                print(f"Appended {stock_symbol} [Bear] with RS: {-1 * rs}, LTP: {last_traded_price}")

    # Sort by RS descending and return top 25
    top_25_stocks = sorted(rs_values, key=lambda x: x["relative_strength"], reverse=True)[:25]

    # Add creation timestamp in IST
    ist = pytz.timezone("Asia/Kolkata")
    created_at = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    # Save the result to a JSON file
    try:
        with open("top_stocks_data.json", "w") as f:
            json.dump({
                "created_at": created_at,
                "data": top_25_stocks
            }, f, indent=4)
            print("Data saved to top_stocks_data.json")
    except Exception as e:
        print(f"Error saving data: {e}")

    return top_25_stocks

@app.get("/get-top-stocks")
def get_top_stocks():
    # Read the results from the saved file
    try:
        with open("top_stocks_data.json", "r") as f:
            top_25_stocks = json.load(f)
            print("Data loaded from top_stocks_data.json")
            return top_25_stocks
    except FileNotFoundError:
        print("File not found. Please run the API first.")
        return {"message": "Data not available. Please run the API first."}
    except Exception as e:
        print(f"Error loading data: {e}")
        return {"message": "Error loading data."}
    

@app.api_route("/sector-strength", methods=["GET", "HEAD"])
def sector_strength():
    sector_rs = []
    nifty_return = calculate_pct_change("^NSEI")

    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)  # last 1 year

    for sector, symbol in sector_indices.items():
        rs = calculate_rs(symbol)

        try:
            data = yf.download(symbol, start=start_date, end=end_date)
            current_price = data['Close'].iloc[-1].item()
            high_52_week = data['High'].max().item()
            low_52_week = data['Low'].min().item()
        except Exception as e:
            print(f"Error fetching sector data for {sector} ({symbol}): {e}")
            current_price = None
            high_52_week = None
            low_52_week = None

        if rs is not None and current_price is not None:
            sector_rs.append({
                "sector": sector,
                "relative_strength": rs if nifty_return > 0 else (-1 * rs),
                "current_price": current_price,
                "52_week_high": high_52_week,
                "52_week_low": low_52_week
            })

    sorted_sectors = sorted(sector_rs, key=lambda x: x["relative_strength"], reverse=True)
    # Add creation timestamp in IST
    ist = pytz.timezone("Asia/Kolkata")
    created_at = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    # Save the result to a JSON file
    try:
        with open("top_sectors_data.json", "w") as f:
            json.dump({
                "created_at": created_at,
                "data": sorted_sectors
            }, f, indent=4)
            print("Data saved to top_sectors_data.json")
    except Exception as e:
        print(f"Error saving data: {e}")
    return sorted_sectors

@app.get("/get-top-sectors")
def get_top_stocks():
    # Read the results from the saved file
    try:
        with open("top_sectors_data.json", "r") as f:
            top_25_stocks = json.load(f)
            print("Data loaded from top_sectors_data.json")
            return top_25_stocks
    except FileNotFoundError:
        print("File not found. Please run the API first.")
        return {"message": "Data not available. Please run the API first."}
    except Exception as e:
        print(f"Error loading data: {e}")
        return {"message": "Error loading data."}

