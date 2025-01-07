#*************************************** OTHER *************************************************************
#US Magnificient 7 or 8 ;-)
MAG_SEVEN = [
    'GOOG',  # Alphabet Inc. Class C (USA)
    'TSLA',  # Tesla, Inc. (USA)
    'AAPL',  # Apple Inc. (USA)
    'META',  # Meta Platforms, Inc. (USA)
    'MSFT',  # Microsoft Corporation (USA)
    'NFLX',  # Netflix, Inc. (USA)
    'NVDA',  # NVIDIA Corporation (USA)
    'AMZN',  # Amazon.com, Inc. (USA)
]

# EU Magnificient 11 known as Granolas
GRANOLAS = [
    'GSK',      # GlaxoSmithKline plc (UK)
    'ROG.SW',   # Roche Holding AG (Switzerland)
    'ASML',     # ASML Holding N.V. (Netherlands)
    'NSRGY',    # Nestlé S.A. (Switzerland - ADR)
    'NVS',      # Novartis AG (Switzerland)
    'NVO',      # Novo Nordisk A/S (Denmark)
    'OR.PA',    # L'Oréal S.A. (France)
    'MC.PA',    # LVMH Moët Hennessy Louis Vuitton (France)
    'AZN',      # AstraZeneca plc (UK)
    'SAP',      # SAP SE (Germany)
    'SNY',      # Sanofi S.A. (France)
]

#*************************************** GREEN - CLIMATE TECH *************************************************************
# ******************************
# Section: Climate Tech Portfolio Definitions
# ******************************
# This section defines portfolios that focus on different themes in climate technology,
# such as solar, wind, and storage. Each portfolio is represented as a list of stock
# tickers, which can be updated as needed to reflect changes in the market.
# these lists are created and maintained by Nicolas Payen. They may not be up-to-date
# some Tickers that generate errors when retrieving data from Yahoo Finance have been removed
#ClimateTech Solar industry
ClimateTech_SOLAR = [
        '000591.SZ',   # Dongfang Electric Corporation (China)
        '000880.KS',   # Hanwha Solutions Corporation (South Korea)
        '002056.SZ',   # Hunan Corun New Energy Co., Ltd. (China)
        '002218.SZ',   # Shunfeng International Clean Energy Ltd. (China)
        '002459.SZ',   # JA Solar Technology Co., Ltd. (China)
        '002518.SZ',   # Kangda New Materials (Group) Co., Ltd. (China)
        '009830.KS',   # Hanwha Q CELLS Co., Ltd. (South Korea)
        '13X.SG',      # Xinyi Solar Holdings Ltd. (Singapore)
#        '1785.TWO',    # Solar Applied Materials Technology Corporation
        '300118.SZ',   # Shenzhen Topraysolar Co., Ltd. (China)
        '300274.SZ',   # Sungrow Power Supply Co., Ltd. (China)
        '300393.SZ',   # Zhejiang Chint Electrics Co., Ltd. (China)
        '300763.SZ',   # Ginlong Technologies Co., Ltd. (China)
        '3800.HK',     # GCL-Poly Energy Holdings Limited (Hong Kong)
        '600438.SS',   # Tongwei Co., Ltd. (China)
        '605117.SS',    # Ningbo Deye Technology Group Co., Ltd. 
        '600732.SS',   # Shanghai Electric Group Company Limited (China)
        '601012.SS',   # LONGi Green Energy Technology Co., Ltd. (China)
        '601615.SS',   # Mingyang Smart Energy Group Co., Ltd. (China)
        '688223.SS',   # Beijing Jingyuntong Technology Co., Ltd. (China)
        '688390.SS',   # Suzhou Maxwell Technologies Co., Ltd. (China)
        '688599.SS',   # Trina Solar Limited (China)
#        '688717.SS',    # solax power network tech
        'AGX',         # Argan, Inc. (USA)
        'AMPS',        # Altus Power, Inc. (USA)
        'ARRY',        # Array Technologies, Inc. (USA)
        'ASTI',        # Ascent Solar Technologies, Inc. (USA)
        'BLDP',        # Ballard Power Systems Inc. (Canada)
        'BSIF.L',      # Bluefield Solar Income Fund Limited (UK)
        'CPV.XA',      # ClearVue Technologies Limited
        'CSIQ',        # Canadian Solar Inc. (Canada)
        'DQ',          # Daqo New Energy Corp. (China)
        'ENPH',        # Enphase Energy, Inc. (USA)
        'FREY',        # FREYR Battery (Norway)
        'FSLR',        # First Solar, Inc. (USA)
        'FTCI',        # FTC Solar Inc. (USA)
        'JKS',         # JinkoSolar Holding Co., Ltd. (China)
        'MAXN',        # Maxeon Solar Technologies, Ltd. (Singapore)
        'MBTN.SW',     # Meyer Burger Technology AG (Switzerland)
        'NESF.L',      # NextEnergy Solar Fund Limited (UK)
        'NOVA',        # Sunnova Energy International Inc. (USA)
        'NXT',         # NextEra Energy, Inc. (USA)
        'ORA',         # Ormat Technologies, Inc. (USA)
        'PLUG',        # Plug Power Inc. (USA)
        'RECSI.OL',    # REC Silicon ASA (Norway)
        'RELIANCE.NS', # Reliance Industries Limited (India)
        'RIGD.IL',     # Rigid Industries Ltd. (Israel)
        'RUN',         # Sunrun Inc. (USA)
        'S92.DE',      # SMA Solar Technology AG (Germany)
        'SEDG',        # SolarEdge Technologies Inc. (Israel)
        'SHLS',        # Shoals Technologies Group, Inc. (USA)
        'SLDP',        # Solid Power, Inc. (USA)
        'SOL',         # ReneSola Ltd. (China)
#        'SOLAR.BK',    # Solartron Public Company Limited
        'SOLARINDS.BO',# Solar Industries India Limited (India)
        'SOLR.V',      # Solar Alliance Energy Inc. (Canada)
        'SOLT.ST',     # SolTech Energy Sweden AB (Sweden)
#        'SPWR',        # SunPower Corporation (USA)
        'TPIC',        # TPI Composites, Inc. (USA)
#       'TTE',          # TotalEnergies SE (France)
        'ZODIAC.NS'    # Zodiac Energy Limited (India)
    ]

#ClimateTech Wind industry
ClimateTech_WIND = [
    '001289.SZ',    # China Datang Corporation Renewable Power Co., Ltd. (China)
    '002531.SZ',    # Tianjin Zhonghuan Semiconductor Co., Ltd. (China)
    '2208.HK',      # Xinjiang Goldwind Science & Technology Co., Ltd. (Hong Kong)
    '2727.HK',      # Shanghai Electric Group Company Limited (Hong Kong)
    '300129.SZ',    # Far East Smarter Energy Co., Ltd. (China)
    '300443.SZ',    # Zhejiang Windey Co., Ltd. (China)
    '300772.SZ',    # Nanjing Turbine & Electric Machinery Group Co., Ltd. (China)
    '601016.SS',    # CECEP Wind-Power Corporation (China)
    '601615.SS',    # Mingyang Smart Energy Group Co., Ltd. (China)
    '688349.SS',    # Jiangsu Zhongtian Technology Co., Ltd. (China)
#   'ÁNA.MC',       # Acciona S.A. (Spain)
    'ENR.DE',       # Siemens Energy AG (Germany)
#    'GE',           # General Electric Company (USA)
    'GEV',          # GE Vernova (USA)
#    'GWIND.IS',    # Gurkan Wind Power (Turkey)
#    '6268.T',       # Nabtesco Corporation (Japan)
    'NDX1.DE',      # Nordex SE (Germany)
    'NRDXF',        # Nordex SE (Germany)
    'SMNEY',        # Siemens Gamesa Renewable Energy, S.A. (Spain)
    'SUZLON.NS',    # Suzlon Energy Limited (India)
    'TKA.DE',       # thyssenkrupp AG (Germany)
    'TPIC',         # TPI Composites, Inc. (USA)
    'UKW.L',        # Greencoat UK Wind PLC (UK)
#    'VWSB.DE',      # 'Vestas Wind Systems A/S (Germany)
    'VWS.CO',      # 'Vestas Wind Systems A/S (Denmark)
    
]

#ClimateTech Energy Storage / wo H2
ClimateTech_STORAGE = [
    '1783.HK',      # Envision Green 
    '002074.SZ',    # Gotion High-Tech Co., Ltd. (China)
    '006400.KS',    # Samsung SDI Co., Ltd. (South Korea)
    '051910.KS',    # LG Chem Ltd. (South Korea)
    '096770.KS',    # SK IE Technology Co., Ltd. (South Korea)
    '300014.SZ',    # Eve Energy Co., Ltd. (China)
    '300207.SZ',    # Shenzhen Deren Electronic Co., Ltd. (China)
    '300750.SZ',    # Contemporary Amperex Technology Co., Limited (CATL) (China)
    '373220.KS',    # LG Energy Solution Ltd. (South Korea)
    '3931.HK',      # China Dynamics Holdings Limited (Hong Kong)
    '6409.TW',      # EVE Energy Co., Ltd. (Taiwan)
    '6752.T',       # Panasonic Corporation (Japan)
    '6674.T',       # GS YUASA (Japan)
    '688006.SS',    # Tianqi Lithium Corporation (China)
    '688390.SS',    # Ganfeng Lithium Co., Ltd. (China)
    '688567.SS',    # Sunwoda Electronic Co., Ltd. (China)
    '605117.SS',    # Ningbo Deye Technology Group Co., Ltd.
    'AQMS',         # Aqua Metals, Inc. 
    'AMPX',         # Amprius Technologies, Inc. (USA)
    'AMY.V',        # American Manganese Inc. (Canada)
    'BES.V',        # Blue Sky Energy Inc. (Canada)
    'BYDDY',        # BYD Company Limited (China)
    'CBAT',         # CBAK Energy Technology, Inc. (China)
    'ENR',          # Energizer Holdings, Inc. (USA)
    'ENVX',         # Enovix Corporation (USA)
    'FLNC',         # Fluence Energy, Inc. (USA)
    'FLUX',         # Flux Power Holdings, Inc. (USA)
    'FREY',         # FREYR Battery (Norway)
    'GRID.L',       # Gresham House Energy Storage Fund plc (UK)
    'GSF.L',        # Gore Street Energy Storage Fund plc (UK)
    'GWH',          # ESS Tech, Inc. (USA)
    'IKA.L',        # iShares Global Clean Energy ETF (UK)
    'ILIKF',        # Ilika plc (UK)
    'NEOV',         # NeoVolta Inc
    'NNOMF',        # Nano One Materials Corp. (Canada)
    'NRGV',         # Energy Vault Holdings, Inc. (USA)
    'NVNXF',        # Novonix Limited (Australia)
    'PLL',          # Piedmont Lithium Inc. (USA)
    'QS',           # QuantumScape Corporation (USA)
    'SLDP',         # Solid Power, Inc. (USA)
    'STEM',         # Stem, Inc. (USA)
    'TSLA',         # Tesla, Inc. (USA)
    'TURB',         # Turbo Energy, S.A.
]

#ClimateTech Grid
ClimateTech_GRID = [
    '015760.KS',    # Korea Electric Power Corporation KEPCO (South Korea)
    '000400.SZ',    # XJ Electric Co., Ltd. (China)
    '298040.KS',    # LS Electric Co., Ltd. (South Korea)
    '600517.SS',    # NARI Technology Co., Ltd. (China)
    '6501.T',       # Hitachi
    'ABBNY',        # ABB Ltd. (Switzerland)
    'AEP',          # American Electric Power Company, Inc. (USA)
    'AGR',          # Avangrid, Inc. (USA)
    'AGX',          # Argan, Inc. (USA)
    'DUK',          # Duke Energy Corporation (USA)
    'ENR.DE',       # Siemens Energy AG (Germany)
    'ENEL.MI',      # Enel Group (Italy)
    'EIX',          # Edison International (USA)
    'EXC',          # Exelon Corporation (USA)
#    'GE',           # General Electric Company (USA)
    'GEV',          # GE Vernova (USA)
    'HUNGF',        # Hungarian Electricity Works (Hungary)
    'IBE.MC',       # Iberdrola, S.A.
    'JYOTISTRUC.NS',# Jyoti Structures Ltd. (India)
    'KEC.NS',       # KEC International Ltd. (India)
    'LT.NS',        # Larsen & Toubro Ltd. (India)
    'NGG',          # National Grid plc (UK)
    'NKT.CO',       # NKT A/S (Denmark)
    'PLPC',         # Preformed Line Products Company (USA)
    'POWL',         # Powell Industries, Inc. (USA)
    'POWERGRID.NS', # Power Grid Corporation of India Ltd. (India)
    'POWERINDIA.NS',# ABB Power Products and Systems India Ltd. (India)
    'PRY.MI',       # Prysmian Group (Italy)
    'PWR',          # Quanta Services, Inc. (USA)
    'RWE.DE',       # RWE AG (Germany)
    'SMNEY',        # Siemens Gamesa Renewable Energy, S.A. (Spain)
    'SO',           # Southern Company (USA)
    'SU.PA',        # Schneider Electric SE (France)
    'XEL',          # Xcel Energy Inc. (USA)
]

#ClimateTech Electric Mobility
ClimateTech_EMOBILITY = [
    '002056.SZ',    # Fujian New Longma Automobile Co., Ltd. (China)
    '300750.SZ',    # Contemporary Amperex Technology Co., Limited (CATL)
    '373220.KS',    # LG Energy Solution Ltd.
    '000270.KS',    # Kia Corporation
    '0175.HK',      # Geely Automobile Holdings Limited (Hong Kong)
    '1810.HK',      # Xiaomi Corporation
    '9863.HK',      # XPeng Inc. (Hong Kong)
    '6752.T',       # Panasonic Corporation
    '688667.SS',    # Changzhou Xingyu Automotive Lighting Systems Co., Ltd. (China)
    'AUR',          # Aurora Innovation, Inc
    'AYRO',         # AYRO, Inc. (USA)
    'BMW.DE',       # Bayerische Motoren Werke AG (Germany)
    'BOSCHLTD.BO',  # Bosch Limited (India)
    'BYDDY',        # BYD Company Limited (China)
    'FUV',          # Arcimoto, Inc. (USA)
    'GOEV',         # Canoo Inc. (USA)')
    'GP',           # GreenPower Motor Company Inc. (Canada)
    'HYLN',         # Hyliion Holdings Corp. (USA)
    'IDEX',         # Ideanomics, Inc. (USA)
    'IKA.L',        # iShares Global Clean Energy ETF (UK)
    'ILIKF',        # Ilika plc (UK)
    'JOBY',         # Joby Aviation, Inc.
    'KNDI',         # Kandi Technologies Group, Inc. (China)
    'LCID',         # Lucid Group, Inc. (USA)
    'LEV',          # Lion Electric Company 
    'LI',           # Li Auto Inc. (China)
    'MBG.DE',       # Mercedes-Benz Group AG (Germany)
    'MBLY',         # Mobileye Global Inc
    'NIO',          # NIO Inc. (China)
    'POAHY',         # Porsche Automobil Holding SE (Germany)
    'PSNY',         # Polestar Automotive Holding UK PLC (Sweden)
#    'PTRA',         # Proterra Inc.
    'QS',           # QuantumScape Corporation (USA)
    'RIVN',         # Rivian Automotive, Inc. (USA)
    'SLDP',         # Solid Power, Inc. (USA)
    'TSLA',         # Tesla, Inc. (USA)
    'UBER',         # Uber Technologies, Inc. (USA)
    'VOW.DE',       # Volkswagen AG (Germany)
    'XPEV',         # XPeng Inc. (China)
]

#ClimateTech EV charging
#remove due to issue with yahoo finance 'RIDE',
ClimateTech_EVCHARGING = [
    '300001.SZ',    # TELD New Energy Co., Ltd
    '6409.TW',      # EVE Energy Co., Ltd. (Taiwan)
    '688390.SS',    # Ganfeng Lithium Co., Ltd. (China)
    'ABBNY',        # ABB Ltd. (Switzerland)
    'ADSE',         # ADS-TEC Energy plc (Germany)
    'ALFEN.AS',     # Alfen N.V.
    'BLNK',         # Blink Charging Co. (USA)
 #   'BP',           # BP Pulse (UK)
    'BOSCHLTD.NS',  # Bosch Limited (India)
    'CHPT',         # ChargePoint Holdings, Inc. (USA)
    'DCFC',         # Tritium DCFC Limited (Australia)
    'EOAN.DE',         # E.ON SE
    'EVGO',         # EVgo Inc. (USA)
    'NAAS',         # NaaS Technology Inc. (China)
    'PODP.L',       # Pod Point Group Holdings plc (UK)
    'SIEGY',        # Siemens AG (Germany)
    'SHLS',         # Shoals Technologies Group, Inc. (USA)
    'TSLA',         # Tesla, Inc. (USA)
    'WBX',          # Wallbox N.V. (Spain)
    'WKHS',         # Workhorse Group Inc. (USA)
    'ZAP.OL',       # Zaptec AS (Norway)
#    'TTE',          # TotalEnergies SE (France)
#    'ENGI',         # Engie SA (France)
 ]


#ClimateTech ELECTRIFICATION & COMMODITY
ClimateTech_ELEC = [
    '000682.SZ',    # Orient Group Inc. (China)
    '002028.SZ',    # Suzhou Anjie Technology Co., Ltd. (China)
    '002358.SZ',    # Shandong Zhangqiu Blower Co., Ltd. (China)
    '002460.SZ',    # Contemporary Amperex Technology Co., Limited (CATL) (China)
    '2727.HK',      # Shanghai Electric Group Company Limited (Hong Kong)
    '298040.KS',    # LS Electric Co., Ltd. (South Korea)
    '329180.KS',    # Hyundai Electric & Energy Systems Co., Ltd. (South Korea)
    '600089.SS',    # TBEA Co., Ltd. (China)
    '600312.SS',    # Pinggao Group Co., Ltd. (China)
    '600406.SS',    # NARI Technology Co., Ltd. (China)
    '601096.SS',    # China Southern Power Grid Energy Co., Ltd. (China)
    '601126.SS',    # China Eastern Airlines Corporation Limited (China)
    '601179.SS',    # China XD Electric Co., Ltd. (China)
    '601567.SS',    # China National Nuclear Power Co., Ltd. (China)
    '601700.SS',    # Changjiang Securities Company Limited (China)
    '601877.SS',    # Zhejiang Chint Electrics Co., Ltd. (China)
    '6409.TW',      # EVE Energy Co., Ltd. (Taiwan)
    '6501.T',       # Hitachi, Ltd. (Japan)
    '6503.T',       # Mitsubishi Electric Corporation (Japan)
    '6594.T',       # Nidec Corporation (Japan)
    '688128.SS',    # China Railway Signal & Communication Corporation Limited (China)
    '688187.SS',    # Shanghai Electric Wind Power Group Co., Ltd. (China)
    '9696.HK',      # Xinyi Solar Holdings Limited (Hong Kong)
    'ABBNY',        # ABB Ltd. (Switzerland)
    'ALB',          # Albemarle Corporation (USA)
    'AMY.V',        # American Manganese Inc. (Canada)
    'BHP',          # BHP Group Limited (Australia)
    'BHP1.F',       # BHP Group Limited (Germany)
    'CETY',         # Clean Energy Technologies, Inc. (USA)
    'DQ',           # Daqo New Energy Corp. (China)
    'E7V0.F',       # Elkem ASA (Germany)
    'ELBM',         # Electra Battery Materials Corporation (Canada)
    'ELHA.AT',      # ElvalHalcor Hellenic Copper and Aluminium Industry S.A. (Greece)
    'ENR.DE',       # Siemens Energy AG (Germany)
    'ELK.OL',       # Elkem ASA (Norway)
    'ETN',          # Eaton Corporation plc (Ireland)
    'GE',           # General Electric Company (USA)
    'GEV',          # GE Vernova (USA)
    'GLNCY',        # Glencore plc (UK)
    'IPWR',         # Ideal Power Inc
    'KOD.L',        # Kodal Minerals plc (UK)
    'LIGHT.AS',     # Signify N.V. (Netherlands)
    'LR.PA',        # Legrand SA (France)
    'MN.V',         # Mason Graphite Inc. (Canada)
    'NDA.DE',       # Aurubis AG (Germany)
    'NGLOY',        # Anglo American plc (UK)
    'NKT.CO',       # NKT A/S (Denmark)
    'NOVA',         # Sunnova Energy International Inc. (USA)
    'PLL',          # Piedmont Lithium Inc. (USA)
    'POWL',         # Powell Industries, Inc. (USA)
    'PRY.MI',       # Prysmian Group (Italy)
    'RCIIND.BO',    # RCI Industries & Technologies Ltd. (India)
    'SGML',         # Sigma Lithium Corporation (Canada)
    'SCCO',         # Southern Copper Corporation (USA)
    'SOLAR-B.CO',   # Solar A/S (Denmark)
    'SQM',          # Sociedad Química y Minera de Chile S.A. (Chile)
    'SU.PA',        # Schneider Electric SE (France)
    'TECK',         # Teck Resources Limited (Canada)
    'VLX.L',        # Volex plc (UK)
    'WCH.DE',       # Wacker Chemie AG (Germany)
    'ZIJMF',        # Zijin Mining Group Company Limited (China)
    '0QWC.IL',      # Elbit Systems Ltd. (Israel)
    '1COV.DE',      # Covestro AG (Germany)
]


#Climate Tech ISOLATION & HEAT PUMP
ClimateTech_HEAT = [
    '000333.SZ',    # Midea Group Co., Ltd.
    '000651.SZ', # Gree Electric Appliances Inc. of Zhuhai
    '000786.SZ',    # Beijing New Building Materials Public Limited Company (China)
    '005930.KS',    # Samsung Electronics Co., Ltd.
    '3300.HK',      # China Resources Cement Holdings Limited (Hong Kong)
    '373220.KS',    # LG Energy Solution Ltd. (South Korea)
    '6367.T',       # Daikin Industries, Ltd. (Japan)
    'AGCO',         # AGCO Corporation (USA)
    'AKE.PA',       # Arkema S.A. (France)
    'BAS.DE',       # BASF SE (Germany)
    'BLUESTARCO.NS',# Blue Star Limited
    'BOSCHLTD.NS',  # Bosch Limited (India)
    'CARR',         # Carrier Global Corporation (USA)
    'IR',           # Ingersoll Rand Inc. (USA)
    'JCI',          # Johnson Controls International plc (Ireland)
#    'KGP.L',        # Kingspan Group plc
    'KYOCY',        # Kyocera Corporation (Japan)
    'NIBE-B.ST',    # NIBE Industrier AB (Sweden)
    'OC',           # Owens Corning
    'ORA',          # Ormat Technologies, Inc. (USA)
    'ROCK-A.CO',    # Rockwool International A/S Class A (Denmark)
    'ROCK-B.CO',    # Rockwool International A/S Class B (Denmark)
    'SGO.PA',       # Saint-Gobain S.A. (France)
    'SKFOF',        # SKF AB (Sweden)
    'SOLB.BR',      # Solvay SA (Belgium)
    'SPXC',         # SPX Technologies, Inc. (USA)
    'TT',           # Trane Technologies plc (USA)
    'VOLTAS.NS',     # Voltas Limited
]

#Algonquin Power & Utilities Corp. (AQN)
#Climate Tech CLEAN INFRA COMPANY
#problem with currency 'PEN.PR', '2082.SR', 'AYDEM.IS'
ClimateTech_INFRA = [
    '000591.SZ',    # Dongfang Electric Corporation (China)
    '001289.SZ',    # China Datang Corporation Renewable Power Co., Ltd. (China)
    '015760.KS',    # Korea Electric Power Corporation (KEPCO) (South Korea)
    '0586.HK',      # China Conch Venture Holdings Limited (Hong Kong)
    '0916.HK',      # China Longyuan Power Group Corporation Limited (Hong Kong)
    '300140.SZ',    # CECEP Environmental Protection Co., Ltd.
    '601016.SS',    # CECEP Wind-power Corporation Co.,Ltd.
    '6838.T',       # Tamagawa Holdings Co., Ltd.
    'ADANIGREEN.NS',# Adani Green Energy Limited (India)
    'AES',          # The AES Corporation
    'AGR',          # Avangrid, Inc. (USA)
    'AMPS',         # Altus Power, Inc. (USA)
    'AMRC',         # Ameresco, Inc. (USA)
    'ANA.MC',       # Acciona S.A. (Spain)
    'AQN',          # Algonquin Power & Utilities Corp. (Canada)
    'AY',           # Atlantica Sustainable Infrastructure plc (UK)
    'BEPC',         # Brookfield Renewable Corporation (Canada)
    'BEPC.TO',      # Brookfield Renewable Corporation (Canada - Toronto)
    'BEP-PA',       # Brookfield Renewable Partners L.P. (USA)
    'BSIF.L',       # Bluefield Solar Income Fund Limited (UK)
    'BYW.DE',       # BayWa AG (Germany)
    'CEG',          # Constellation Energy Corporation (USA)
    'CWEN',         # Clearway Energy, Inc. (USA)
    'CWEN-A',       # Clearway Energy, Inc. Class A (USA)
    'ECV.DE',       # Encavis AG
    'EDPR.LS',      # EDP Renováveis S.A. (Spain)
    'ENGI.PA',      # Engie SA (France)
    'ENEL.MI',      # Enel S.p.A. (Italy)
    'EVGRF',        # Enviva Inc. (USA)
    'FSFL.L',       # Foresight Solar Fund Limited (UK)
    'GRID.L',       # Gresham House Energy Storage Fund plc (UK)
    'IBDRY',        # Iberdrola, S.A. (Spain)
    'JLEN.L',       # JLEN Environmental Assets Group Limited (UK)
    'NEE',          # NextEra Energy, Inc. (USA)
    'NEP',          # NextEra Energy Partner (US)
    'NEOEN.PA',     # Neoen S.A. (France)
    'NESF.L',       # NextEnergy Solar Fund Limited (UK)
    'NHY.OL',       # Norsk Hydro ASA (Norway)
    'NSOL.OL',      # NorSun AS (Norway)
    'ORA',          # Ormat Technologies, Inc. (USA)
    'ORIT.L',       # Octopus Renewables Infrastructure Trust plc (UK)
    'ORSTED.CO',    # Ørsted A/S (Denmark)
    'RIGD.IL',      # Rigid Industries Ltd. (Israel)
    'RNW',          # TransAlta Renewables Inc. (Canada)
    'RWE.DE',       # RWE AG (Germany)
    'SCATC.OL',     # Scatec ASA (Norway)
    'SGO.PA',       # Saint-Gobain S.A. (France)
    'TRIG.L',       # The Renewables Infrastructure Group Limited (UK)
#    'TTE',          # TotalEnergies SE (France)
    'VLTSA.PA',     # Voltalia S.A. (France)
    'WM',           # Waste Management
]

#Climate Tech POWER UTILITIES
#ClimateTech_POWER = ['OEWA.F', 'FOJCF', '600900.SS', '015760.KS', 'WEC', 'ED', 'PCG', 'XEL', 'NGG', 'AEP', 'SRE', 'D', 'SO', 'NEE-PR', 'DUK', '0MC5.IL']
#remove due to issue 'AESC'
ClimateTech_POWER = [
    '0002.HK',      # CLP Holdings Limited (Hong Kong)
    '015760.KS',    # Korea Electric Power Corporation (KEPCO) (South Korea)
    '600900.SS',    # China Yangtze Power Co., Ltd. (China)
    '9501.T',       # Tokyo Electric Power Company Holdings, Inc. (Japan)
    'AEP',          # American Electric Power Company, Inc. (USA)
    'AGL.AX',       # AGL Energy Limited (Australia)
    'D',            # Dominion Energy, Inc. (USA)
    'DUK',          # Duke Energy Corporation (USA)
    'ED',           # Consolidated Edison, Inc. (USA)
    'ENEL.MI',      # Enel S.p.A. (Italy)
    'EXC',          # Exelon Corporation (USA)
    'FOJCF',        # Fortis Inc. (Canada)
    'IBE.MC',       # Iberdrola, S.A. (Spain)
    'NGG',          # National Grid plc (UK)
    'NEE-PR',       # NextEra Energy, Inc. Preferred Shares (USA)
    'NEE',          # NextEra Energy, Inc. Preferred Shares (USA)
    'OEWA.F',       # EWE AG (Germany)
    'PCG',          # PG&E Corporation (USA)
    'PPL',          # PPL Corporation (USA)
    'SRE',          # Sempra Energy (USA)
    'SO',           # Southern Company (USA)
    'WEC',          # WEC Energy Group, Inc. (USA)
    'XEL',          # Xcel Energy Inc. (USA)
    'NTPC.NS',      # NTPC Limited (India)
    'POWERGRID.NS', # Power Grid Corporation of India Limited (India)
    'TATAPOWER.NS', # Tata Power Company Limited (India)
    'ADANIPOWER.NS',# Adani Power Limited (India)
    'RPOWER.NS',    # Reliance Power Limited (India)
]

#Climate Tech NUCLEAR
#ClimateTech_NUCL = ['FOJCF', 'UEC', '0611.HK', '601611.SS', 'PALAF', 'SMR', '015760.KS', '000881.SZ', 'UCLE', 'NLR', '601985.SS', 'CCJ', 'UUUU', 'DNN']
ClimateTech_NUCL = [
    '000881.SZ',    # Datang International Power Generation Co., Ltd. (China)
    '015760.KS',    # Korea Electric Power Corporation (KEPCO) (South Korea)
    '0611.HK',      # China Nuclear Energy Technology Corporation Limited (Hong Kong)
    '601611.SS',    # China National Nuclear Power Co., Ltd. (China)
    '601985.SS',    # China General Nuclear Power Corporation (CGN) (China)
    'BWXT',         # BWX Technologies, Inc. (USA)
    'CCJ',          # Cameco Corporation (Canada)
    'CEG',          # Constellation Energy Corporation (USA)
    'DNN',          # Denison Mines Corp. (Canada)
    'FLR',          # Fluor Corporation (USA)
    'FOJCF',        # Fortis Inc. (Canada)
#    'NLR',          # VanEck Vectors Uranium+Nuclear Energy ETF (USA)
    'PALAF',        # Paladin Energy Ltd. (Australia)
    'SMR',          # NuScale Power Corporation (USA)
    'UCLE',         # US Nuclear Corp. (USA)
    'UEC',          # Uranium Energy Corporation (USA)
    'URA',          # Global X Uranium ETF (USA)
    'UUUU',         # Energy Fuels Inc. (USA)
    'VST',          # Vistra Corp. (USA)
]

#Climate Tech WASTE
ClimateTech_WASTE = [
    '0K8W.IL',      # Shikun & Binui Water Ltd. (Israel)
    '0257.HK',      # China Everbright Environment Group Limited (Hong Kong)
    '300190.SZ',    # Changsha Zoomlion Heavy Industry Science and Technology Co., Ltd. (China)
    '5857.T',       # Adachi Co., Ltd. (Japan)
    '6564.T',       # Mixi, Inc. (Japan)
    '9221.T',       # Fuji Clean Co., Ltd. (Japan)
    '9336.T',       # Sansui Electric Co., Ltd. (Japan)
    '9247.T',       # Ishizuka Glass Co., Ltd. (Japan)
    'AWHCL.BO',     # Antony Waste Handling Cell Limited (India)
    'CLG.AX',       # Cleanaway Waste Management Limited (Australia)
    'CWY.AX',       # Cleanaway Waste Management Limited (Australia)
    'CWST',         # Casella Waste Systems, Inc. (USA)
    'DBG.PA',       # Derichebourg SA
    'GFL',          # GFL Environmental Inc. (Canada)
    'MEG',          # Montrose Environmental Group, Inc. (USA)
    'NORVA.ST',     # Norva24 Group AB (Sweden)
    'RSG',          # Republic Services, Inc. (USA)
    'RWI.AS',       # Renewi plc (Netherlands)
    'SRCL',         # Stericycle, Inc. (USA)
    'SY9.F',        # Symrise AG (Germany)
    'VEOEY',        # Veolia Environnement S.A. (France)
    'WCN',          # Waste Connections, Inc. (USA)
    'WM',           # Waste Management, Inc. (USA)
    'CLH',          # Clean Harbors, Inc. (USA
#    'SEV',          # Suez Environment
    'SGM.AX',       # Sims Limited (Australia)
]

#Climate Tech CLEAN FUEL
ClimateTech_CleanFUEL = [
    '600688.SS',  # Sinopec Shanghai Petrochemical Company Limited (China)
    '7012.T',     # Kawasaki Heavy Industries, Ltd. (Japan)
    'CLNE',       # Clean Energy Fuels Corp. (USA)
    'EQT.L',      # EQTEC plc (UK)
    'GRN.TO',     # Greenlane Renewables Inc. (Canada)
    'HLGN',       # Heliogen, Inc. (USA)
    'ITM.L',      # ITM Power plc (UK)
    'NEL.OL',     # Nel ASA (Norway)
    'ORA',        # Ormat Technologies, Inc. (USA)
    'PHE.L',      # PowerHouse Energy Group plc (UK)
    'PLUG',       # Plug Power Inc. (USA)
    'PYR.TO',     # PyroGenesis Canada Inc. (Canada)
    'VSL.L',      # Velocys plc (UK)
]

#Climate Tech GREEN HYDROGEN
ClimateTech_HTWO = [
    '601012.SS',   # LONGi Green Energy Technology Co., Ltd. (China)
    '8088.T',      # Iwatani Corporatio
    '005380.KS',   # Hanwha Solutions Corporation
    'AFC.L',       # AFC Energy plc (UK)
    'AI.PA',       # Air Liquide S.A. (France)
    'APD',         # Air Products and Chemicals, Inc. (USA)
    'ATOM.L',      # ATOME Energy plc (UK)
    'BE',          # Bloom Energy Corporation (USA)
    'BLDP',        # Ballard Power Systems Inc. (Canada)
    'CMI',         # Cummins Inc. (USA)
    'CPH2.L',      # Clean Power Hydrogen plc (UK)
    'CWR.L',       # Ceres Power Holdings plc (UK)
    'ENR.DE',      # Siemens Energy AG (Germany)
    'FCEL',        # FuelCell Energy, Inc. (USA)
    'GREENH.CO',   # Green Hydrogen Systems A/S (Denmark)
    'H2O.DE',      # HydrogenPro AS (Germany)
    'HGEN.L',      # HydrogenOne Capital Growth plc (UK)
    'HLGN',        # Heliogen, Inc. (USA)
    'ITM.L',       # ITM Power plc (UK)
    'LIN',         # Linde plc (Germany/Global)
    'NEL.OL',      # Nel ASA (Norway)
    'PLUG',        # Plug Power Inc. (USA)
    'SMNEY',       # Siemens Gamesa Renewable Energy, S.A. (Spain)
    'TKA.DE',      # thyssenkrupp AG (Germany)
    'VSL.L',       # Velocys plc (UK)
]

#Climate Tech WATER
ClimateTech_WATER = [
    '0270.HK',  # Guangdong Investment Limited (Hong Kong)
    '0371.HK',  # Beijing Enterprises Water Group Limited (China)
    '0807.HK',  # China Everbright Water Limited (Hong Kong)
    '0855.HK',  # China Water Affairs Group Limited (Hong Kong)
    '021240.KS', # Coway Co., Ltd. (South Korea)
    '034020.KS', # Doosan Heavy Industries & Construction Co., Ltd. (South Korea)
    '300070.SZ', # Beijing OriginWater Technology Co., Ltd. (China)
    '3402.T',    # Toray Industries, Inc. (Japan)
    '6370.T',    # Kurita Water Industries Ltd. (Japan)
    '6501.T',    # Hitachi, Ltd. (Japan)
    'AWK',       # American Water Works Company, Inc. (USA)
#    'EcoLab',    # Ecolab Inc.
    'BJWTF',     # Beijing Enterprises Water Group Limited (China - OTC)
 #   'Pentair',   # Pentair plc
    'VEOEY',     # Veolia Environnement S.A. (France)
    'VLTO',      # Veralto Corporation (USA)
    'XYL',       # Xylem Inc. (USA)
]

#*************************************** AI *************************************************************
# ******************************
# Section: AI, Automation, Robotic
# ******************************
#automation and robotic 
Automation_Robotic = [
    '000150.KS',  # Doosan Robotics (South Korea)
    '300124.SZ',  # Shenzhen Inovance Technology Co., Ltd. (China)
    '6201.T',     # Yaskawa Electric Corporation (Japan)
    '6506.T',     # Yokogawa Electric Corporation (Japan)
    '6861.T',     # Keyence Corporation (Japan)
    '6954.T',     # Fanuc Corporation (Japan)
    'ABBNY',      # ABB Ltd. (Switzerland)
    'CDNS',       # Cadence Design Systems, Inc. (USA)
    'DNZOF',      # Fanuc Corporation (Japan ADR)
    'EMR',        # Emerson Electric Co. (USA)
    'FANUY',      # Fanuc Corporation (USA ADR)
    'FICO',       # Fair Isaac Corporation (USA)
    'ISRG',       # Intuitive Surgical, Inc. (USA)
    'KWHIY',      # Kawasaki Heavy Industries, Ltd. (Japan ADR)
#    'KU2.DE',     # KUKA AG (Germany)
    'MBLY',       # Mobileye Global Inc. (USA)
    'MSBHF',      # Mitsubishi Electric Corporation (Japan)
    'NVDA',       # NVIDIA Corporation (USA)
    'OMRNY',      # Omron Corporation (Japan ADR)
    'PDYN',       # Paradox Interactive AB (Sweden)
    'ROK',        # Rockwell Automation, Inc. (USA)
#   'RWLK', 
    'SEKEY',      # Sekisui Chemical Co., Ltd. (Japan ADR)
    'SIE.DE',     # Siemens AG (Germany)
    'TSLA',       # Tesla, Inc. (USA)
]

#Artifical Intelligence (AI)
Artificial_Intelligence = [
    '005930.KS',  # Samsung Electronics Co., Ltd. (South Korea)
    '2317.TW',    # Hon Hai Precision Industry Co., Ltd. (Taiwan)
    '2330.TW',    # Taiwan Semiconductor Manufacturing Company Limited (Taiwan)
    'ADBE',       # Adobe Inc. (USA)
    'AI',         # C3.ai, Inc. (USA)
    'AMD',        # Advanced Micro Devices, Inc. (USA)
    'AME',        # AMETEK, Inc. (USA)
    'AMZN',       # Amazon.com, Inc. (USA)
    'ANET',       # Arista Networks, Inc. (USA)
    'ANSS',       # ANSYS, Inc. (USA)
    'ASML',       # ASML Holding N.V. (Netherlands)
    'BABA',       # Alibaba Group Holding Limited (China)
    'BIDU',       # Baidu, Inc. (China)
    'DIDIY',      # DiDi Global Inc. (China)
    'EQIX',       # Equinix, Inc. (USA)
    'GOOG',       # Alphabet Inc. Class C (USA)
    'IBM',        # International Business Machines Corporation (USA)
    'INTC',       # Intel Corporation (USA)
    'ISRG',       # Intuitive Surgical, Inc. (USA)
    'LUMN',       # Lumen Technologies, Inc. (USA)
    'META',       # Meta Platforms, Inc. (USA)
    'MRVL',       # Marvell Technology, Inc. (USA)
    'MSFT',       # Microsoft Corporation (USA)
    'NVDA',       # NVIDIA Corporation (USA)
    'PLTR',       # Palantir Technologies Inc. (USA)
    'SMCI',       # Super Micro Computer, Inc. (USA)
    'SNOW',       # Snowflake Inc. (USA)
    'SOI.PA',     # Soitec S.A. (France)
    'SYM',        # Symbotic Inc. (USA)
    'TSLA',       # Tesla, Inc. (USA)
    'UPST',       # Upstart Holdings, Inc. (USA)
]

#*************************************** HEALTHCARE *************************************************************
#healthcare - Health Tech
HealthTech = [
    '300760.SZ',     # Mindray Bio-Medical Electronics Co., Ltd
    '603259.SS',    # WuXi AppTec Co., Ltd.
    '4543.T',       # Terumo Corporation
    '7733.T',       # Olympus Corporation
    '6869.T',       # Sysmex Corporation
    'A',            # Agilent Technologies, Inc. (USA)
    'ABBV',         # AbbVie Inc. (USA)
    'ABT',          # Abbott Laboratories (USA)
    'ACCD',         # Accolade, Inc. (USA)
#    'AGTI',         # Agiliti, Inc. (USA)
    'AKYA',         # Akoya Biosciences, Inc. (USA)
    'ALC',          # Alcon Inc. (Switzerland)
    'ALGN',         # Align Technology, Inc. (USA)
    'AMGN',         # Amgen Inc. (USA)
    'ANGO',         # AngioDynamics, Inc. (USA)
    'ANIK',         # Anika Therapeutics, Inc. (USA)
    'ATEC',         # Alphatec Holdings, Inc. (USA)
    'ATR',          # AptarGroup, Inc. (USA)
#    'ATRI',         # Atrion Corporation (USA)
    'AXNX',         # Axonics, Inc. (USA)
    'AZN',          # AstraZeneca plc (UK)
    'AZTA',         # Azenta, Inc. (USA)
    'BAX',          # Baxter International Inc. (USA)
    'BDX',          # Becton, Dickinson and Company (USA)
    'BIO',          # Bio-Rad Laboratories, Inc. Class A (USA)
    'BIO-B',        # Bio-Rad Laboratories, Inc. Class B (USA)
    'BLCO',         # Bausch + Lomb Corporation (Canada)
    'BMY',          # Bristol-Myers Squibb Company (USA)
    'BRKR',         # Bruker Corporation (USA)
    'BSX',          # Boston Scientific Corporation (USA)
    'BTSG',         # Biotage AB (Sweden)
    'CERT',         # Certara, Inc. (USA)
    'CGON',         # Cogent Biosciences, Inc. (USA)
    'CI',           # Cigna Group (USA)
    'CMAX',         # CareMax, Inc. (USA)
    'CNMD',         # CONMED Corporation (USA)
    'COO',          # CooperCompanies, Inc. (USA)
#    'CPSI',         # Computer Programs and Systems, Inc. (USA)
    'DGX',          # Quest Diagnostics Incorporated (USA)
    'DH',           # Definitive Healthcare Corp. (USA)
    'DHR',          # Danaher Corporation (USA)
    'DOCS',         # Doximity, Inc. (USA)
    'DRW3.DE',      # Drägerwerk AG & Co. KGaA (Germany)
    'DXCM',         # Dexcom, Inc. (USA)
    'EMBC',         # Embecta Corp. (USA)
    'EVH',          # Evolent Health, Inc. (USA)
    'EW',           # Edwards Lifesciences Corporation (USA)
    'FME.DE',       # Fresenius Medical Care AG & Co. KGaA (Germany)
    'GDRX',         # GoodRx Holdings, Inc. (USA)
    'GEHC',         # GE HealthCare Technologies Inc. (USA)
    'GETI-B.ST',    # Getinge AB (Sweden)
    'GILD',         # Gilead Sciences, Inc. (USA)
    'GKOS',         # Glaukos Corporation (USA)
    'GMED',         # Globus Medical, Inc. (USA)
    'GN.CO',        # GN Store Nord A/S (Denmark)
    'HAE',          # Haemonetics Corporation (USA)
    'HCA',          # HCA Healthcare, Inc. (USA)
    'HCAT',         # Health Catalyst, Inc. (USA)
    'HQY',          # HealthEquity, Inc. (USA)
    'HSTM',         # HealthStream, Inc. (USA)
    'ICUI',         # ICU Medical, Inc. (USA)
    'IDXX',         # IDEXX Laboratories, Inc. (USA)
    'INSP',         # Inspire Medical Systems, Inc. (USA)
    'IQV',          # IQVIA Holdings Inc. (USA)
    'IRTC',         # iRhythm Technologies, Inc. (USA)
    'ISRG',         # Intuitive Surgical, Inc. (USA)
    'ITGR',         # Integer Holdings Corporation (USA)
    'JNJ',          # Johnson & Johnson (USA)
    'PHIA.AS',      # Koninklijke Philips N.V. (Netherlands)
    'LIVN',         # LivaNova PLC (UK)
    'LLY',          # Eli Lilly and Company (USA)
    'MASI',         # Masimo Corporation (USA)
    'MDRX',         # Allscripts Healthcare Solutions, Inc. (USA)
    'MDT',          # Medtronic plc (Ireland)
    'MMSI',         # Merit Medical Systems, Inc. (USA)
    'MRK',          # Merck & Co., Inc. (USA)
    'MTD',          # Mettler-Toledo International Inc. (USA)
    'MYGN',         # Myriad Genetics, Inc. (USA)
    'NARI',   # Inari Medical, Inc. (USA)
    'NRC',    # National Research Corporation (USA)
    'NVST',   # Envista Holdings Corporation (USA)
    'OMCL',   # Omnicell, Inc. (USA)
    'OSUR',   # OraSure Technologies, Inc. (USA)
    'PEN',    # Penumbra, Inc. (USA)
    'PGNY',   # Progyny, Inc. (USA)  
    'PHR',    # Phreesia, Inc. (USA)
    'PINC',   # Premier, Inc. (USA)
    'PODD',   # Insulet Corporation (USA)
    'PRVA',   # Privia Health Group, Inc. (USA)
    'QDEL',   # QuidelOrtho Corporation (USA)
    'RCM',    # R1 RCM Inc. (USA)
    'REGN',   # Regeneron Pharmaceuticals, Inc. (USA)
    'RGEN',   # Repligen Corporation (USA)
    'RMD',    # ResMed Inc. (USA)
    'RVTY',   # Revvity, Inc. (USA)
    'SDGR',   # Schrodinger, Inc. (USA)
    'SHC',    # Sotera Health Company (USA)
    'SHL.DE', # Siemens Healthineers AG (Germany)
    'SLP',    # Simulations Plus, Inc. (USA)
    'SN.L',   # Smith & Nephew plc (UK)
    'SNN',    # Smith & Nephew plc (UK)
    'SPOK',   # Spok Holdings, Inc. (USA)
    'SRT3.DE',# Sartorius AG (Germany)
    'STE',    # STERIS plc (USA)
    'STVN',   # Stevanato Group S.p.A. (Italy)
    'STMN.SW',# Straumann Holding AG (Switzerland)
#    'SWAV',  # ShockWave Medical, Inc. (USA)
    'SYK',    # Stryker Corporation (USA)
    'TDOC',   # Teladoc Health, Inc. (USA)
    'TFX',    # Teleflex Incorporated (USA)
    'THC',    # Tenet Healthcare Corporation (USA)
    'TMO',    # Thermo Fisher Scientific Inc. (USA)
    'TXG',    # 10x Genomics, Inc. (USA)
    'UTMD',   # Utah Medical Products, Inc. (USA)
    'VEEV',   # Veeva Systems Inc. (USA)
    'VRTX',   # Vertex Pharmaceuticals Incorporated (USA)
    'WAT',    # Waters Corporation (USA)
    'WRBY',   # Warby Parker Inc. (USA)
    'WST',    # West Pharmaceutical Services, Inc. (USA)
    'XRAY',   # Dentsply Sirona Inc. (USA)
    'ZBH',    # Zimmer Biomet Holdings, Inc. (USA)
]

#healthcare - Health Infra
HealthInfra = [
    '4568.T',   # Daiichi Sankyo Co., Ltd. 
    '1099.HK',  # China National Pharmaceutical Group Corp (Sinopharm) 
    'CHCT',     # Community Healthcare Trust
    'CTRE',     # CareTrust REIT
    'DOC',      # Physicians Realty Trust
    'FRE.DE',   # Fresenius SE & Co. KGaA
    'GMRE',     # Global Medical REIT
    'GMRE-PA',  # Global Medical REIT Preferred
    'HR',       # Healthcare Realty Trust
    'IART',     # Integra LifeSciences
    'LTC',      # LTC Properties
    'LH',       # Laboratory Corporation of America
#    'MDC.L',     # Mediclinic International
    'MDT',      # Medtronic PLC
    'NHI',      # National Health Investors
    'OHI',      # Omega Healthcare Investors
    'ORP2.VI',  # emeis Société anonyme
#    'PEAK',     # Healthpeak Properties
    'RHCPA.AX', # Ramsay Healthcare Limited
    'SBRA',     # Sabra Health Care REIT
    'THC',      # Tenet Healthcare Corporation
    'VTR',      # Ventas, Inc.
    'WELL',     # Welltower Inc.
    'UHT',      # Universal Health Realty Income Trust
]

#healthcare - Health Care
HealthCare = [
    'ALHC',  # Align HealthCare
    'CAH',   # Cardinal Health
    'CNC',   # Centene Corporation
    'COR',   # Corindus Vascular Robotics
    'CRL',   # Charles River Laboratories
    'CVS',   # CVS Health
    'ELV',   # Elevance Health
    'GH',    # Guardant Health
    'GSK',   # GlaxoSmithKline
    'HSIC',  # Henry Schein, Inc.
    'HUM',   # Humana
    'ICLR',  # ICON plc
    'MCK',   # McKesson Corporation
    'MOH',   # Molina Healthcare
    'NEUE',  # NeuBase Therapeutics
    'OMI',   # Owens & Minor
    'OSCR',  # Oscar Health
    'PDCO',  # Patterson Companies
    'PFE',   # Pfizer Inc.
    'SNY',   # Sanofi
    'UNH',   # UnitedHealth Group
    'ZYXI'   # Zynex, Inc.
]

#healthcare molecule
HealthDrug = [
#    'ACOR',  # Acorda Therapeutics Inc.
    'ALKS',  # Alkermes plc
    'AMPH',  # Amphastar Pharmaceuticals Inc.
    'AMRX',  # Amneal Pharmaceuticals Inc.
    'BHC',   # Bausch Health Companies Inc.
    'BIIB',  # Biogen Inc.
    'COLL',  # Collegium Pharmaceutical Inc.
    'CTLT',  # Catalent Inc.
#    'DCPH',  # Deciphera Pharmaceuticals Inc.
    'DVAX',  # Dynavax Technologies Corporation
    'ELAN',  # Elanco Animal Health Incorporated
    'EVO',   # Evotec SE
    'HCM',   # HUTCHMED (China) Limited
    'HLN',   # Haleon plc
    'ILMN',  # Illumina Inc.
    'INDV',  # Indivior plc
    'IRWD',  # Ironwood Pharmaceuticals Inc.
    'ITCI',  # Intra-Cellular Therapies Inc.
    'KMDA',  # Kamada Ltd.
    'LFCR',  # Lifecore Biomedical Inc.
    'MEDP',  # Medpace Holdings Inc.
    'MRNA',  # Moderna Inc.
    'NBIX',  # Neurocrine Biosciences Inc.
    'NEOG',  # Neogen Corporation
    'NTRA',  # Natera Inc.
    'NVO',   # Novo Nordisk A/S
    'NVS',   # Novartis AG
    'PBH',   # Prestige Consumer Healthcare Inc.
    'PCRX',  # Pacira BioSciences Inc.
    'PETQ',  # PetIQ Inc.
    'PRGO',  # Perrigo Company plc
    'QGEN',  # Qiagen N.V.
    'RDY',   # Dr. Reddy's Laboratories Ltd.
    'TAK',   # Takeda Pharmaceutical Co. Ltd.
#    'TARO',  # Taro Pharmaceutical Industries Ltd.
    'TEVA',  # Teva Pharmaceutical Industries Ltd.
    'TWST',  # Twist Bioscience Corporation
    'VTRS',  # Viatris Inc.
    'ZTS',   # Zoetis Inc.
    # Additional Prominent Drug Makers
    'SAN.PA',  # Sanofi S.A. (France)
    'AZN',     # AstraZeneca plc (UK)
    'NOVN.SW', # Novartis AG (Switzerland)
    'BAYN.DE', # Bayer AG (Germany)
    'ROG.SW',  # Roche Holding AG (Switzerland)
    'JNJ',     # Johnson & Johnson (USA)
    'ABBV',    # AbbVie Inc. (USA)
    'GILD',    # Gilead Sciences Inc. (USA)
    'LLY',     # Eli Lilly and Company (USA)
    'MRK',     # Merck & Co. Inc. (USA)
    '4502.T',  # Takeda Pharmaceutical Co. Ltd. (Japan)
    '4503.T',  # Astellas Pharma Inc. (Japan)
    '4523.T',  # Eisai Co. Ltd. (Japan)
#    'DRRD.NS', # Dr. Reddy's Laboratories Ltd. (India)
    'CIPLA.NS',# Cipla Ltd. (India)
    'SUNPHARMA.NS', # Sun Pharmaceutical Industries Ltd. (India)
]


#*************************************** Gratification *************************************************************
Gratifications = [
    # Fashion and Leather Goods
    'MC.PA',    # LVMH Moët Hennessy Louis Vuitton SE (France)
    'KER.PA',   # Kering SA (France)
    'CPRI',     # Capri Holdings Limited (USA)
    'TPR',      # Tapestry, Inc. (USA)
    'BRBY.L',   # Burberry Group plc (UK)
    '1913.HK',  # Prada S.p.A. (Hong Kong)
    'RL',       # Ralph Lauren Corporation (USA)
    'RMS.PA',   # Hermès International S.A. (France)
    'MONC.MI',  # Moncler S.p.A. (Italy)
#    'TOD.MI',   # Tod's S.p.A. (Italy)

    # Jewelry and Watches
    'CFR.SW',   # Compagnie Financière Richemont SA (Switzerland)
    'UHR.SW',   # The Swatch Group Ltd. (Switzerland)
    'PANDY',    # Pandora A/S (Denmark)
    'SIG',      # Signet Jewelers Limited (USA)

    # Automobiles
    'RACE',     # Ferrari N.V. (Italy)
    'P911.DE',  # Porsche AG
    'BMW.DE',   # Bayerische Motoren Werke AG (Germany)
    'MBG.DE',   # Mercedes-Benz Group AG (Germany)
    'TSLA',     # Tesla, Inc. (USA)
    'TATAMOTORS.NS',      # Tata Motors Limited (India)
    'HMC',      # Honda Motor Co., Ltd. (Japan)
    'TM',       # Toyota Motor Corporation (Japan)

    # Hospitality
    'MAR',      # Marriott International, Inc. (USA)
    'HLT',      # Hilton Worldwide Holdings Inc. (USA)
    'IHG',      # InterContinental Hotels Group PLC (UK)
    'H',        # Hyatt Hotels Corporation (USA)
    'AC.PA',    # Accor SA (France)
    'MLCO',     # Melco Resorts & Entertainment Limited (Hong Kong)
    'LVS',      # Las Vegas Sands Corp. (USA)
    'WYNN',     # Wynn Resorts, Limited (USA)
    'MGM',      # MGM Resorts International (USA)

    # Real Estate
    'VNO',      # Vornado Realty Trust (USA)
    'HKHGF',    # Hongkong Land Holdings Limited (Hong Kong)
    'SPG',      # Simon Property Group, Inc. (USA)
    'BXP',      # Boston Properties, Inc. (USA)
    '1113.HK',  # CK Asset Holdings Limited (Hong Kong)
    'CPP.F',    # China Overseas Land & Investment Limited (Hong Kong)
    'ARE',      # Alexandria Real Estate Equities, Inc. (USA)
    'EQR',      # Equity Residential (USA)

    # Luxury Spirits and Beverages
    'BF-B',     # Brown-Forman Corporation (USA)
    'DEO',      # Diageo plc (UK)
    'RI.PA',    # Pernod Ricard SA (France)
    'CCU',      # Compañía Cervecerías Unidas S.A. (Chile)
    '2503.T',   # Kirin Holdings Company, Limited (Japan)
#    'SAB',     # SABMiller plc (UK) [Acquired by Anheuser-Busch InBev]
    'TAP',      # Molson Coors Beverage Company (USA)
    'ABEV',     # Ambev S.A. (Brazil)
    'HEIA.AS',  # Heineken N.V. (Netherlands)
    'CBGB.F',   # Carlsberg A/S (Denmark)
    '2502.T',    # Asahi Group Holdings, Ltd. (Japan)
    '600600.SS', # Tsingtao Brewery Company Limited (China)
    '002304.SZ', # Jiangsu Yanghe Brewery Joint-Stock Co., Ltd. (China)
    '600519.SS', # Kweichow Moutai Co., Ltd. (China)

    # Beauty and Cosmetics
    'SSDOY',    # Shiseido Company, Limited (Japan)
    '002790.KS' # AMOREPACIFIC Group (South Korea)
]

#*************************************** Generational *************************************************************
# Baby Boomers Companies
Generation_W_Companies = [
    'KO',   # The Coca-Cola Company
    'PEP',  # PepsiCo, Inc.
    'MCD',  # McDonald's Corporation
    'F',    # Ford Motor Company
    'GM',   # General Motors Company
    'JNJ',  # Johnson & Johnson
    'PG',   # Procter & Gamble Co.
    'IBM',  # International Business Machines Corporation
    'DIS',  # The Walt Disney Company
    'T',    # AT&T Inc.
    'WMT',  # Walmart Inc.
    'MO',   # Altria Group, Inc.
    'DEO',  # Diageo plc
#   'SAB',  # SABMiller plc
    'TM',   # Toyota Motor Corporation
    '005930.KS',  # Samsung Electronics Co., Ltd.
    'UL',   # Unilever plc
    'NVS',  # Novartis AG
]

# Generation X Companies
Generation_X_Companies = [
    'AAPL',     # Apple Inc.
    'NKE',      # Nike, Inc.
    'SONY',     # Sony Group Corporation
    'MSFT',     # Microsoft Corporation
    'SBUX',     # Starbucks Corporation
    'ADBE',     # Adobe Inc.
    'EA',       # Electronic Arts Inc.
    'HAS',      # Hasbro, Inc.
    'BMW.DE',   # Bayerische Motoren Werke AG
    'GOOG',     # Alphabet Inc.
#    'ATVI',     # Activision Blizzard, Inc.
    'NFLX',     # Netflix, Inc.
    'RL',       # Ralph Lauren Corporation
    '005930.KS', # Samsung Electronics Co., Ltd.
    'DIS',      # The Walt Disney Company
    'DEO',      # Diageo plc
    '7974.T',   # Nintendo Co., Ltd.
    'MC.PA',  # LVMH Moët Hennessy Louis Vuitton SE
    'KER.PA',   # Kering SA
    'RMS.PA',   # Hermès International S.A.
]

# Millennials Companies
Generation_Y_Companies = [
    'META',  # Meta Platforms, Inc.
    'NFLX', # Netflix, Inc.
    'TSLA',  # Tesla, Inc.
    'AMZN',  # Amazon.com, Inc.
    'BKNG',  # Booking Inc.
    'SPOT',  # Spotify Technology S.A.
    'AAPL',  # Apple Inc.
    'UBER',  # Uber Technologies, Inc.
    'ADSK',  # Autodesk, Inc.
    'LULU',  # Lululemon Athletica Inc.
    'SQ',    # Block, Inc.
#   'TWTR',  # Twitter, Inc.
    'ETSY',  # Etsy, Inc.
    'PYPL',  # PayPal Holdings, Inc.
    '1810.HK',  # Xiaomi Corporation
    'TCEHY',    # Tencent Holdings Limited
    'MNSO',     # Miniso Group Holding Limited
    '1913.HK',  # Prada S.p.A.
    'RL',       # Ralph Lauren Corporation
    'RACE',     # Ferrari N.V.
]

# Generation Z Companies
Generation_Z_Companies = [
    'SNAP',  # Snap Inc.
    'BILI',  # Bilibili Inc.
    'BYND',  # Beyond Meat, Inc.
    'SPOT',  # Spotify Technology S.A.
    'RBLX',  # Roblox Corporation
    'ABNB',  # AirBnB Inc.
    'MTCH',  # Match Group, Inc.
    'SHOP',  # Shopify Inc.
    'NVDA',  # NVIDIA Corporation
    'Z',     # Zillow Group, Inc.
    'PLTR',  # Palantir Technologies Inc.
    'DIS',   # The Walt Disney Company
    '005930.KS',  # Samsung Electronics Co., Ltd.
    '035900.KS', #JYP ENTERTAIN ORD (Kpop)
    '7974.T',# Nintendo Co., Ltd.
    'MNSO',  # Miniso Group Holding Limited
    'BABA',  # Alibaba Group Holding Limited
    'JD',    # JD.com, Inc.
    'PDD',   # Pinduoduo Inc.
    'TME',  # Tencent Music Entertainment Group
    'IQ',    # iQIYI, Inc.
    'ETH-USD',  # Ethereum Cryptocurrency
    'BTC-USD',  # Bitcoin Cryptocurrency
    'COIN',  # Coinbase Global, Inc.
    'MNST',  # Monster Beverage Corporation

]

#*************************************** FOSSIL FUEL *************************************************************
#Coal
#removed due to issue: 'GMETCOAL.BO'
COAL = [
    # Coal Mining Companies
    'GLNCY',    # Glencore plc
    '3315.T',   # Mitsubishi Corporation
    'AMR',      # Alpha Metallurgical Resources, Inc.
    'SXC',      # SunCoke Energy, Inc.
    'SOL.AX',   # Washington H. Soul Pattinson and Company Limited
    'CRN.AX',   # Coronado Global Resources Inc.
    'SMR.AX',   # Stanmore Resources Limited
    'YAL.AX',   # Yancoal Australia Ltd
    'NHC.AX',   # New Hope Corporation Limited
    'NC',       # NACCO Industries, Inc.
    'NRP',      # Natural Resource Partners L.P.
    'CEIX',     # CONSOL Energy Inc.
    'ARLP',     # Alliance Resource Partners, L.P.
    'BTU',      # Peabody Energy Corporation
    'HCC',      # Warrior Met Coal, Inc.
    'METC',     # Ramaco Resources, Inc.
    'ARCH',     # Arch Resources, Inc.
]

#O&G
#removed due to error 'BOIL.L', 'PMOIF', 'SOI','SBOW','CPE',
OIL_GAS = [
    # From your original list
    '096770.KS',  # SK Innovation Co., Ltd. (South Korea)
    '2222.SR',    # Saudi Aramco (Saudi Arabia)
    'AETUF',      # ARC Resources Ltd. (Canada)
    'AOIFF',      # Africa Oil Corp. (Canada)
    'ATHOF',      # Athabasca Oil Corporation (Canada)
    'ATGFF',      # Advantage Energy Ltd. (Canada)
    'ATO',        # Atmos Energy Corporation (USA)
    'BKR',        # Baker Hughes Company (USA)
    'BIREF',      # Birchcliff Energy Ltd. (Canada)
    'BP',         # BP p.l.c. (UK)
    'CVI',        # CVR Energy, Inc. (USA)
    'CHRD',       # Chord Energy Corporation (USA)
    'CNNEF',      # Canadian Natural Resources Limited (Canada)
    'CRLFF',      # Cardinal Energy Ltd. (Canada)
    'CRNCY',      # Crescent Energy Inc. (USA)
    'CTRA',       # Coterra Energy Inc. (USA)
    'CWEGF',      # Crew Energy Inc. (Canada)
    'CVX',        # Chevron Corporation (USA)
    'DVN',        # Devon Energy Corporation (USA)
    'E',          # Eni S.p.A. (Italy)
    'EC',         # Ecopetrol S.A. (Colombia)
    'EE',         # Excelerate Energy, Inc. (USA)
    'EQT',        # EQT Corporation (USA)
    'EQNR',       # Equinor ASA (Norway)
    'FANG',       # Diamondback Energy, Inc. (USA)
    'FTI',        # TechnipFMC plc (UK)
    'FRHLF',      # Freehold Royalties Ltd. (Canada)
    'GENGF',      # Genesis Energy, L.P. (USA)
    'GLNCY',      # Glencore plc (UK)
    'HPK',        # HighPeak Energy, Inc. (USA)
    'IMPP',       # Imperial Petroleum Inc. (Greece)
    'IMO',        # Imperial Oil Limited (Canada)
    'IPO.TO',     # InPlay Oil Corp. (Canada)
    'JRNGF',      # Journey Energy Inc. (Canada)
    'KEYUF',      # Keyera Corp. (Canada)
    'MEGEF',      # MEG Energy Corp. (Canada)
    'MGY',        # Magnolia Oil & Gas Corporation (USA)
    'MPC',        # Marathon Petroleum Corporation (USA)
    'NHC.AX',     # New Hope Corporation Limited (Australia)
    'NTPC.NS',    # NTPC Limited (India)
    'OXY',        # Occidental Petroleum Corporation (USA)
    'PARR',       # Par Pacific Holdings, Inc. (USA)
    'PBF',        # PBF Energy Inc. (USA)
    'PBR-A',      # Petróleo Brasileiro S.A. - Petrobras (Preferred Shares) (Brazil)
    'PEYUF',      # Peyto Exploration & Development Corp. (Canada)
    'PMGYF',      # Paramount Resources Ltd. (Canada)
    'PTEN',       # Patterson-UTI Energy, Inc. (USA)
    'PUMP',       # ProPetro Holding Corp. (USA)
    'SAVE.L',     # Savannah Energy Plc (UK)
    'SLB',        # Schlumberger N.V. (USA)
    'SM',         # SM Energy Company (USA)
    'SNPMF',      # Sinopec Shanghai Petrochemical Company Limited (China)
    'SHEL',       # Shell plc (UK)
    'SPGYF',      # Spartan Delta Corp. (Canada)
    'SPM.MI',     # Saipem S.p.A. (Italy)
    'STOHF',      # Santos Ltd. (Australia)
    'SUN',        # Sunoco LP (USA)
    'TALO',       # Talos Energy Inc. (USA)
    'TNEYF',      # Tenaris S.A. (Luxembourg)
    'TRMLF',      # Tamarack Valley Energy Ltd. (Canada)
    'TRP',        # TC Energy Corporation (Canada)
    'TUWOY',      # Tullow Oil plc (UK)
    'TUWLF',      # TransAlta Renewables Inc. (Canada)
    'VAL',        # Valaris Limited (USA)
    'VET',        # Vermilion Energy Inc. (Canada)
    'VLO',        # Valero Energy Corporation (USA)
    'WFRD',       # Weatherford International plc (USA)
    'WTTR',       # Select Energy Services, Inc. (USA)
    'XOM',        # Exxon Mobil Corporation (USA)
    'ZPTAF',      # Topaz Energy Corp. (Canada)

    # Additional players 
    'SU',     # Suncor Energy Inc. (Canada)
    'LNG',    # Cheniere Energy, Inc. (USA)
    'WMB',    # The Williams Companies, Inc. (USA)
    'EPD',    # Enterprise Products Partners L.P. (USA)
#   'MMP',    # Magellan Midstream Partners, L.P. (USA)
    'PSX',    # Phillips 66 (USA)
#    'ANDV',   # Andeavor (USA)
    'YPF',    # YPF Sociedad Anónima (Argentina)
#     'HFC',    # HollyFrontier Corporation (USA)
]

