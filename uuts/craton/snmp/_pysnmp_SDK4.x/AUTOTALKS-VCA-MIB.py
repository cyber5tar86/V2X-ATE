# PySNMP SMI module. Autogenerated from smidump -f python AUTOTALKS-VCA-MIB
# by libsmi2pysnmp-0.1.3 at Mon Feb  9 11:49:26 2015,
# Python version sys.version_info(major=2, minor=7, micro=3, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( atlkMgmt, ) = mibBuilder.importSymbols("AUTOTALKS-REG", "atlkMgmt")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue")

# Objects

vcaMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 38405, 1, 5)).setRevisions(("2014-03-13 00:00","2013-11-19 00:00","2012-12-20 00:00",))
if mibBuilder.loadTexts: vcaMib.setOrganization("Autotalks")
if mibBuilder.loadTexts: vcaMib.setContactInfo("Grand Netter Building\nPOB 3846, Kfar-Netter 40593, Israel\nPhone: (+972)-9-886-5300\nFax:   (+972)-9-886-5301\ninfo@auto-talks.com")
if mibBuilder.loadTexts: vcaMib.setDescription("VCA (V2X Communication Analyzer) MIB.")
vcaConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 5, 1))
vcaGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 5, 1, 1))
vcaCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 5, 1, 2))
vcaRx = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 5, 2))
vcaBsmRxEnabled = MibScalar((1, 3, 6, 1, 4, 1, 38405, 1, 5, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcaBsmRxEnabled.setDescription("Whether BSM reception is enabled.")
vcaLogMode = MibScalar((1, 3, 6, 1, 4, 1, 38405, 1, 5, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,0,)).subtype(namedValues=NamedValues(("off", 0), ("ifHasNavFix", 1), ("ifHasTrueTime", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcaLogMode.setDescription("VCA logging modes:\n\noff -- No logging.\nifHasNavFix -- Log only when navigation fix is available.\nifHasTrueTime -- Log only when true (UTC) time is available.")
vcaIfTable = MibTable((1, 3, 6, 1, 4, 1, 38405, 1, 5, 4))
if mibBuilder.loadTexts: vcaIfTable.setDescription("A table with a row for each V2X MAC interface in the system.")
vcaIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 38405, 1, 5, 4, 1)).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vcaIfEntry.setDescription("VCA management infromation per each V2X MAC interface.")
vcaTxPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 38405, 1, 5, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcaTxPeriod.setDescription("Time period between sequential VCA frame transmissions.")
vcaFrameLen = MibTableColumn((1, 3, 6, 1, 4, 1, 38405, 1, 5, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(40, 2304))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcaFrameLen.setDescription("Length of IEEE 802.11 MSDU generated by VCA.")
vcaTxEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 38405, 1, 5, 4, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vcaTxEnabled.setDescription("Whether VCA frame transmission from this MAC interface is enabled.")

# Augmentions

# Groups

vcaMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 38405, 1, 5, 1, 1, 1)).setObjects(*(("AUTOTALKS-VCA-MIB", "vcaFrameLen"), ("AUTOTALKS-VCA-MIB", "vcaBsmRxEnabled"), ("AUTOTALKS-VCA-MIB", "vcaTxEnabled"), ("AUTOTALKS-VCA-MIB", "vcaTxPeriod"), ("AUTOTALKS-VCA-MIB", "vcaLogMode"), ) )
if mibBuilder.loadTexts: vcaMibGroup.setDescription("All objects in AUTOTALKS-VCA-MIB")

# Compliances

vcaCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 38405, 1, 5, 1, 2, 1)).setObjects(*(("AUTOTALKS-VCA-MIB", "vcaMibGroup"), ) )
if mibBuilder.loadTexts: vcaCompliance.setDescription("Compliance statement covering entire AUTOTALKS-VCA-MIB")

# Exports

# Module identity
mibBuilder.exportSymbols("AUTOTALKS-VCA-MIB", PYSNMP_MODULE_ID=vcaMib)

# Objects
mibBuilder.exportSymbols("AUTOTALKS-VCA-MIB", vcaMib=vcaMib, vcaConformance=vcaConformance, vcaGroups=vcaGroups, vcaCompliances=vcaCompliances, vcaRx=vcaRx, vcaBsmRxEnabled=vcaBsmRxEnabled, vcaLogMode=vcaLogMode, vcaIfTable=vcaIfTable, vcaIfEntry=vcaIfEntry, vcaTxPeriod=vcaTxPeriod, vcaFrameLen=vcaFrameLen, vcaTxEnabled=vcaTxEnabled)

# Groups
mibBuilder.exportSymbols("AUTOTALKS-VCA-MIB", vcaMibGroup=vcaMibGroup)

# Compliances
mibBuilder.exportSymbols("AUTOTALKS-VCA-MIB", vcaCompliance=vcaCompliance)
