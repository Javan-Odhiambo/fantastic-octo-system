import requests

# ----------------------------------------------------------------------------
# ******************************* URLS START *******************************
# ----------------------------------------------------------------------------

HOST = 'https://192.168.100.1'
GET_LOGIN_TOKEN_URL = HOST + "/asp/GetRandCount.asp"
LOGIN_URL = HOST + '/login.cgi'
POST_SETTINGS_URL = HOST + '/html/bbsp/wan/complex.cgi?y=InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1&RequestFile=html/bbsp/wan/confirmwancfginfo.html'
MAIN_PAGE_URL = HOST + '/CustomApp/mainpage.asp'


# ----------------------------------------------------------------------------
# ********************************* URLS END *********************************
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# ******************************* DATA START *******************************
# ----------------------------------------------------------------------------


LOGIN_TOKEN = requests.post(GET_LOGIN_TOKEN_URL , verify=False).text.lstrip('\ufeff')
LOGIN_DATA = {
    'UserName': 'telecomadmin',
    'PassWord': 'YWRtaW50ZWxlY29t',
    'Language': 'english',
    'x.X_HW_Token': LOGIN_TOKEN
}


# ----------------------------------------------------------------------------
# ******************************** DATA END ********************************
# ----------------------------------------------------------------------------




# ----------------------------------------------------------------------------
# ****************************** HEADERS START *******************************
# ----------------------------------------------------------------------------


COMMON_HEADER = {
    'Host': '192.168.100.1',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://192.168.100.1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
}


LOGIN_HEADER = {
    'Content-Length': '126',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://192.168.100.1/',
}
LOGIN_HEADER.update(COMMON_HEADER)


SETTINGS_HEADER = {
    'Content-Length': '633',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://192.168.100.1/html/bbsp/wan/wan.asp',
}
SETTINGS_HEADER.update(COMMON_HEADER)


# ----------------------------------------------------------------------------
# ******************************* HEADERS END ********************************
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# ***************************** POST DATA START ******************************
# ----------------------------------------------------------------------------


settings_data = {
    'y.Enable': '1',
    'y.X_HW_IPv4Enable': '1',
    'y.X_HW_IPv6Enable': '0',
    'y.X_HW_IPv6MultiCastVLAN': '-1',
    'y.X_HW_SERVICELIST': 'INTERNET',
    'y.X_HW_ExServiceList': '',
    'y.X_HW_VLAN': '10',
    'y.X_HW_PRI': '0',
    'y.X_HW_PriPolicy': 'Specified',
    'y.X_HW_DefaultPri': '0',
    'y.ConnectionType': 'IP_Routed',
    'y.X_HW_MultiCastVLAN': '4294967295',
    'y.NATEnabled': '1',
    'y.X_HW_NatType': '0',
    'y.Username': '',
    'y.Password': '4f8224e09511627bd85daa3dea225ed3fb3be608f8f103df4d061ae7bf508065',
    'y.X_HW_LcpEchoReqCheck': '0',
    'y.ConnectionTrigger': 'AlwaysOn',
    'y.DNSEnabled': '1',
    'y.MaxMRUSize': '1500',
    'y.DNSOverrideAllowed': '0',
    'y.DNSServers': ',',
    'y.X_HW_BindPhyPortInfo': '',
    'X_HW_OverrideAllowed': '0',
    'x.X_HW_Token': ''
}

# ----------------------------------------------------------------------------
# ****************************** POST DATA END *******************************
# ----------------------------------------------------------------------------

