# PySNMP SMI module. Autogenerated from smidump -f python AUTOTALKS-RSVC-MIB
# by libsmi2pysnmp-0.1.3 at Tue Aug  4 15:19:14 2015,
# Python version sys.version_info(major=2, minor=7, micro=6, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( atlkMgmt, ) = mibBuilder.importSymbols("AUTOTALKS-REG", "atlkMgmt")
( LinkProtocolId, ) = mibBuilder.importSymbols("AUTOTALKS-TC", "LinkProtocolId")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( InetAddressIPv4, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv4", "InetPortNumber")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( RowStatus, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue")

# Types

class RsvcObjIndex(TextualConvention, Integer32):
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(1,65535)
    

# Objects

rsvcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 38405, 1, 7)).setRevisions(("2015-07-06 00:00",))
if mibBuilder.loadTexts: rsvcMib.setOrganization("Autotalks")
if mibBuilder.loadTexts: rsvcMib.setContactInfo("Grand Netter Building\nPOB 3846, Kfar-Netter 40593, Israel\nPhone: (+972)-9-886-5300\nFax:   (+972)-9-886-5301\ninfo@auto-talks.com")
if mibBuilder.loadTexts: rsvcMib.setDescription("Autotalks Remote Services MIB.")
rsvcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 7, 1))
rsvcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 7, 1, 1))
rsvcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 7, 1, 2))
rsvcSmt = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 7, 2))
rsvcDefaultDestIpAddressIPv4 = MibScalar((1, 3, 6, 1, 4, 1, 38405, 1, 7, 2, 1), InetAddressIPv4()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsvcDefaultDestIpAddressIPv4.setDescription("Default destination IPv4 address for Remote Services messages.")
rsvcWlan = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 7, 3))
rsvcWlanFwdTable = MibTable((1, 3, 6, 1, 4, 1, 38405, 1, 7, 3, 2))
if mibBuilder.loadTexts: rsvcWlanFwdTable.setDescription("WLAN packet forwarding table.")
rsvcWlanFwdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 38405, 1, 7, 3, 2, 1)).setIndexNames((0, "AUTOTALKS-RSVC-MIB", "rsvcWlanFwdIndex"))
if mibBuilder.loadTexts: rsvcWlanFwdEntry.setDescription("WLAN packet forwarding entry.")
rsvcWlanFwdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 38405, 1, 7, 3, 2, 1, 1), RsvcObjIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: rsvcWlanFwdIndex.setDescription("Identifies row of WLAN packet forwarding table.")
rsvcWlanFwdDestPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 38405, 1, 7, 3, 2, 1, 2), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsvcWlanFwdDestPortNumber.setDescription("Destination port for forwarded WLAN packets.")
rsvcWlanFwdIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 38405, 1, 7, 3, 2, 1, 3), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsvcWlanFwdIfIndex.setDescription("WLAN MAC interface index.")
rsvcWlanFwdFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 38405, 1, 7, 3, 2, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,0,)).subtype(namedValues=NamedValues(("data", 0), ("vsa", 1), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsvcWlanFwdFrameType.setDescription("WLAN frame type.")
rsvcWlanFwdProtocolId = MibTableColumn((1, 3, 6, 1, 4, 1, 38405, 1, 7, 3, 2, 1, 5), LinkProtocolId()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsvcWlanFwdProtocolId.setDescription("WLAN packet protocol ID.")
rsvcWlanFwdRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 38405, 1, 7, 3, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsvcWlanFwdRowStatus.setDescription("WLAN packet forwarding conceptual row status.")

# Augmentions

# Groups

rsvcMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 38405, 1, 7, 1, 1, 1)).setObjects(*(("AUTOTALKS-RSVC-MIB", "rsvcWlanFwdIfIndex"), ("AUTOTALKS-RSVC-MIB", "rsvcWlanFwdProtocolId"), ("AUTOTALKS-RSVC-MIB", "rsvcDefaultDestIpAddressIPv4"), ("AUTOTALKS-RSVC-MIB", "rsvcWlanFwdFrameType"), ("AUTOTALKS-RSVC-MIB", "rsvcWlanFwdDestPortNumber"), ("AUTOTALKS-RSVC-MIB", "rsvcWlanFwdRowStatus"), ) )
if mibBuilder.loadTexts: rsvcMibGroup.setDescription("Remote services management objects.")

# Compliances

rsvcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 38405, 1, 7, 1, 2, 1)).setObjects(*(("AUTOTALKS-RSVC-MIB", "rsvcMibGroup"), ) )
if mibBuilder.loadTexts: rsvcCompliance.setDescription("Compliance statement covering entire AUTOTALKS-RSVC-MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("AUTOTALKS-RSVC-MIB", PYSNMP_MODULE_ID=rsvcMib)

# Types
mibBuilder.exportSymbols("AUTOTALKS-RSVC-MIB", RsvcObjIndex=RsvcObjIndex)

# Objects
mibBuilder.exportSymbols("AUTOTALKS-RSVC-MIB", rsvcMib=rsvcMib, rsvcConformance=rsvcConformance, rsvcGroups=rsvcGroups, rsvcCompliances=rsvcCompliances, rsvcSmt=rsvcSmt, rsvcDefaultDestIpAddressIPv4=rsvcDefaultDestIpAddressIPv4, rsvcWlan=rsvcWlan, rsvcWlanFwdTable=rsvcWlanFwdTable, rsvcWlanFwdEntry=rsvcWlanFwdEntry, rsvcWlanFwdIndex=rsvcWlanFwdIndex, rsvcWlanFwdDestPortNumber=rsvcWlanFwdDestPortNumber, rsvcWlanFwdIfIndex=rsvcWlanFwdIfIndex, rsvcWlanFwdFrameType=rsvcWlanFwdFrameType, rsvcWlanFwdProtocolId=rsvcWlanFwdProtocolId, rsvcWlanFwdRowStatus=rsvcWlanFwdRowStatus)

# Groups
mibBuilder.exportSymbols("AUTOTALKS-RSVC-MIB", rsvcMibGroup=rsvcMibGroup)

# Compliances
mibBuilder.exportSymbols("AUTOTALKS-RSVC-MIB", rsvcCompliance=rsvcCompliance)
