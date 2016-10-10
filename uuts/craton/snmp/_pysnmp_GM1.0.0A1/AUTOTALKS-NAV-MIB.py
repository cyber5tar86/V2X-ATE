# PySNMP SMI module. Autogenerated from smidump -f python AUTOTALKS-NAV-MIB
# by libsmi2pysnmp-0.1.3 at Sun Aug 25 17:51:48 2013,
# Python version sys.version_info(major=2, minor=7, micro=3, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( atlkMgmt, ) = mibBuilder.importSymbols("AUTOTALKS-REG", "atlkMgmt")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue")

# Objects

navMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 38405, 1, 6)).setRevisions(("2013-04-21 00:00",))
if mibBuilder.loadTexts: navMib.setOrganization("Autotalks")
if mibBuilder.loadTexts: navMib.setContactInfo("Grand Netter Building\nPOB 3846, Kfar-Netter 40593, Israel\nPhone: (+972)-9-886-5300\nFax:   (+972)-9-886-5301\ninfo@auto-talks.com")
if mibBuilder.loadTexts: navMib.setDescription("Navigation MIB.")
navConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 6, 1))
navGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 6, 1, 1))
navCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 38405, 1, 6, 1, 2))
navFixAvailable = MibScalar((1, 3, 6, 1, 4, 1, 38405, 1, 6, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: navFixAvailable.setDescription("Whether a navigation fix is available (via satellite navigation and/or\nanother method).")

# Augmentions

# Groups

navMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 38405, 1, 6, 1, 1, 1)).setObjects(*(("AUTOTALKS-NAV-MIB", "navFixAvailable"), ) )
if mibBuilder.loadTexts: navMibGroup.setDescription("All objects in AUTOTALKS-NAV-MIB")

# Compliances

navCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 38405, 1, 6, 1, 2, 1)).setObjects(*(("AUTOTALKS-NAV-MIB", "navMibGroup"), ) )
if mibBuilder.loadTexts: navCompliance.setDescription("Compliance statement covering entire AUTOTALKS-NAV-MIB")

# Exports

# Module identity
mibBuilder.exportSymbols("AUTOTALKS-NAV-MIB", PYSNMP_MODULE_ID=navMib)

# Objects
mibBuilder.exportSymbols("AUTOTALKS-NAV-MIB", navMib=navMib, navConformance=navConformance, navGroups=navGroups, navCompliances=navCompliances, navFixAvailable=navFixAvailable)

# Groups
mibBuilder.exportSymbols("AUTOTALKS-NAV-MIB", navMibGroup=navMibGroup)

# Compliances
mibBuilder.exportSymbols("AUTOTALKS-NAV-MIB", navCompliance=navCompliance)
