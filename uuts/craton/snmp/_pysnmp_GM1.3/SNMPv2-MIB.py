# PySNMP SMI module. Autogenerated from smidump -f python SNMPv2-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jan 14 14:42:00 2014,
# Python version sys.version_info(major=2, minor=7, micro=3, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, mib_2, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "mib-2", "snmpModules")
( DisplayString, TestAndIncr, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TestAndIncr", "TimeStamp")

# Objects

system = MibIdentifier((1, 3, 6, 1, 2, 1, 1))
sysDescr = MibScalar((1, 3, 6, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDescr.setDescription("A textual description of the entity.  This value should\ninclude the full name and version identification of\nthe system's hardware type, software operating-system,\nand networking software.")
sysObjectID = MibScalar((1, 3, 6, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysObjectID.setDescription("The vendor's authoritative identification of the\nnetwork management subsystem contained in the entity.\nThis value is allocated within the SMI enterprises\nsubtree (1.3.6.1.4.1) and provides an easy and\nunambiguous means for determining `what kind of box' is\nbeing managed.  For example, if vendor `Flintstones,\nInc.' was assigned the subtree 1.3.6.1.4.1.424242,\nit could assign the identifier 1.3.6.1.4.1.424242.1.1\nto its `Fred Router'.")
sysUpTime = MibScalar((1, 3, 6, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUpTime.setDescription("The time (in hundredths of a second) since the\nnetwork management portion of the system was last\nre-initialized.")
sysContact = MibScalar((1, 3, 6, 1, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysContact.setDescription("The textual identification of the contact person for\nthis managed node, together with information on how\nto contact this person.  If no contact information is\nknown, the value is the zero-length string.")
sysName = MibScalar((1, 3, 6, 1, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysName.setDescription("An administratively-assigned name for this managed\nnode.  By convention, this is the node's fully-qualified\ndomain name.  If the name is unknown, the value is\nthe zero-length string.")
sysLocation = MibScalar((1, 3, 6, 1, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysLocation.setDescription("The physical location of this node (e.g., 'telephone\ncloset, 3rd floor').  If the location is unknown, the\nvalue is the zero-length string.")
sysServices = MibScalar((1, 3, 6, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysServices.setDescription("A value which indicates the set of services that this\nentity may potentially offer.  The value is a sum.\n\nThis sum initially takes the value zero. Then, for\neach layer, L, in the range 1 through 7, that this node\nperforms transactions for, 2 raised to (L - 1) is added\nto the sum.  For example, a node which performs only\nrouting functions would have a value of 4 (2^(3-1)).\nIn contrast, a node which is a host offering application\nservices would have a value of 72 (2^(4-1) + 2^(7-1)).\nNote that in the context of the Internet suite of\nprotocols, values should be calculated accordingly:\n\n     layer      functionality\n       1        physical (e.g., repeaters)\n       2        datalink/subnetwork (e.g., bridges)\n       3        internet (e.g., supports the IP)\n       4        end-to-end  (e.g., supports the TCP)\n       7        applications (e.g., supports the SMTP)\n\nFor systems including OSI protocols, layers 5 and 6\nmay also be counted.")
sysORLastChange = MibScalar((1, 3, 6, 1, 2, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysORLastChange.setDescription("The value of sysUpTime at the time of the most recent\nchange in state or value of any instance of sysORID.")
sysORTable = MibTable((1, 3, 6, 1, 2, 1, 1, 9))
if mibBuilder.loadTexts: sysORTable.setDescription("The (conceptual) table listing the capabilities of\nthe local SNMP application acting as a command\nresponder with respect to various MIB modules.\nSNMP entities having dynamically-configurable support\nof MIB modules will have a dynamically-varying number\nof conceptual rows.")
sysOREntry = MibTableRow((1, 3, 6, 1, 2, 1, 1, 9, 1)).setIndexNames((0, "SNMPv2-MIB", "sysORIndex"))
if mibBuilder.loadTexts: sysOREntry.setDescription("An entry (conceptual row) in the sysORTable.")
sysORIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sysORIndex.setDescription("The auxiliary variable used for identifying instances\nof the columnar objects in the sysORTable.")
sysORID = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysORID.setDescription("An authoritative identification of a capabilities\nstatement with respect to various MIB modules supported\nby the local SNMP application acting as a command\nresponder.")
sysORDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysORDescr.setDescription("A textual description of the capabilities identified\nby the corresponding instance of sysORID.")
sysORUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 1, 9, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysORUpTime.setDescription("The value of sysUpTime at the time this conceptual\nrow was last instantiated.")
snmp = MibIdentifier((1, 3, 6, 1, 2, 1, 11))
snmpInPkts = MibScalar((1, 3, 6, 1, 2, 1, 11, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInPkts.setDescription("The total number of messages delivered to the SNMP\nentity from the transport service.")
snmpOutPkts = MibScalar((1, 3, 6, 1, 2, 1, 11, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutPkts.setDescription("The total number of SNMP Messages which were\npassed from the SNMP protocol entity to the\ntransport service.")
snmpInBadVersions = MibScalar((1, 3, 6, 1, 2, 1, 11, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInBadVersions.setDescription("The total number of SNMP messages which were delivered\nto the SNMP entity and were for an unsupported SNMP\nversion.")
snmpInBadCommunityNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInBadCommunityNames.setDescription("The total number of community-based SNMP messages (for\nexample,  SNMPv1) delivered to the SNMP entity which\nused an SNMP community name not known to said entity.\nAlso, implementations which authenticate community-based\nSNMP messages using check(s) in addition to matching\nthe community name (for example, by also checking\nwhether the message originated from a transport address\nallowed to use a specified community name) MAY include\nin this value the number of messages which failed the\nadditional check(s).  It is strongly RECOMMENDED that\n\nthe documentation for any security model which is used\nto authenticate community-based SNMP messages specify\nthe precise conditions that contribute to this value.")
snmpInBadCommunityUses = MibScalar((1, 3, 6, 1, 2, 1, 11, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInBadCommunityUses.setDescription("The total number of community-based SNMP messages (for\nexample, SNMPv1) delivered to the SNMP entity which\nrepresented an SNMP operation that was not allowed for\nthe SNMP community named in the message.  The precise\nconditions under which this counter is incremented\n(if at all) depend on how the SNMP entity implements\nits access control mechanism and how its applications\ninteract with that access control mechanism.  It is\nstrongly RECOMMENDED that the documentation for any\naccess control mechanism which is used to control access\nto and visibility of MIB instrumentation specify the\nprecise conditions that contribute to this value.")
snmpInASNParseErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInASNParseErrs.setDescription("The total number of ASN.1 or BER errors encountered by\nthe SNMP entity when decoding received SNMP messages.")
snmpInTooBigs = MibScalar((1, 3, 6, 1, 2, 1, 11, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInTooBigs.setDescription("The total number of SNMP PDUs which were\ndelivered to the SNMP protocol entity and for\nwhich the value of the error-status field was\n`tooBig'.")
snmpInNoSuchNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInNoSuchNames.setDescription("The total number of SNMP PDUs which were\ndelivered to the SNMP protocol entity and for\nwhich the value of the error-status field was\n`noSuchName'.")
snmpInBadValues = MibScalar((1, 3, 6, 1, 2, 1, 11, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInBadValues.setDescription("The total number of SNMP PDUs which were\ndelivered to the SNMP protocol entity and for\nwhich the value of the error-status field was\n`badValue'.")
snmpInReadOnlys = MibScalar((1, 3, 6, 1, 2, 1, 11, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInReadOnlys.setDescription("The total number valid SNMP PDUs which were delivered\nto the SNMP protocol entity and for which the value\nof the error-status field was `readOnly'.  It should\nbe noted that it is a protocol error to generate an\nSNMP PDU which contains the value `readOnly' in the\nerror-status field, as such this object is provided\nas a means of detecting incorrect implementations of\nthe SNMP.")
snmpInGenErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInGenErrs.setDescription("The total number of SNMP PDUs which were delivered\nto the SNMP protocol entity and for which the value\nof the error-status field was `genErr'.")
snmpInTotalReqVars = MibScalar((1, 3, 6, 1, 2, 1, 11, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInTotalReqVars.setDescription("The total number of MIB objects which have been\nretrieved successfully by the SNMP protocol entity\nas the result of receiving valid SNMP Get-Request\nand Get-Next PDUs.")
snmpInTotalSetVars = MibScalar((1, 3, 6, 1, 2, 1, 11, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInTotalSetVars.setDescription("The total number of MIB objects which have been\naltered successfully by the SNMP protocol entity as\nthe result of receiving valid SNMP Set-Request PDUs.")
snmpInGetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInGetRequests.setDescription("The total number of SNMP Get-Request PDUs which\nhave been accepted and processed by the SNMP\nprotocol entity.")
snmpInGetNexts = MibScalar((1, 3, 6, 1, 2, 1, 11, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInGetNexts.setDescription("The total number of SNMP Get-Next PDUs which have been\naccepted and processed by the SNMP protocol entity.")
snmpInSetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInSetRequests.setDescription("The total number of SNMP Set-Request PDUs which\nhave been accepted and processed by the SNMP protocol\nentity.")
snmpInGetResponses = MibScalar((1, 3, 6, 1, 2, 1, 11, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInGetResponses.setDescription("The total number of SNMP Get-Response PDUs which\nhave been accepted and processed by the SNMP protocol\nentity.")
snmpInTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInTraps.setDescription("The total number of SNMP Trap PDUs which have been\naccepted and processed by the SNMP protocol entity.")
snmpOutTooBigs = MibScalar((1, 3, 6, 1, 2, 1, 11, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutTooBigs.setDescription("The total number of SNMP PDUs which were generated\nby the SNMP protocol entity and for which the value\nof the error-status field was `tooBig.'")
snmpOutNoSuchNames = MibScalar((1, 3, 6, 1, 2, 1, 11, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutNoSuchNames.setDescription("The total number of SNMP PDUs which were generated\nby the SNMP protocol entity and for which the value\nof the error-status was `noSuchName'.")
snmpOutBadValues = MibScalar((1, 3, 6, 1, 2, 1, 11, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutBadValues.setDescription("The total number of SNMP PDUs which were generated\nby the SNMP protocol entity and for which the value\nof the error-status field was `badValue'.")
snmpOutGenErrs = MibScalar((1, 3, 6, 1, 2, 1, 11, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutGenErrs.setDescription("The total number of SNMP PDUs which were generated\nby the SNMP protocol entity and for which the value\nof the error-status field was `genErr'.")
snmpOutGetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutGetRequests.setDescription("The total number of SNMP Get-Request PDUs which\nhave been generated by the SNMP protocol entity.")
snmpOutGetNexts = MibScalar((1, 3, 6, 1, 2, 1, 11, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutGetNexts.setDescription("The total number of SNMP Get-Next PDUs which have\nbeen generated by the SNMP protocol entity.")
snmpOutSetRequests = MibScalar((1, 3, 6, 1, 2, 1, 11, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutSetRequests.setDescription("The total number of SNMP Set-Request PDUs which\nhave been generated by the SNMP protocol entity.")
snmpOutGetResponses = MibScalar((1, 3, 6, 1, 2, 1, 11, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutGetResponses.setDescription("The total number of SNMP Get-Response PDUs which\nhave been generated by the SNMP protocol entity.")
snmpOutTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpOutTraps.setDescription("The total number of SNMP Trap PDUs which have\nbeen generated by the SNMP protocol entity.")
snmpEnableAuthenTraps = MibScalar((1, 3, 6, 1, 2, 1, 11, 30), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpEnableAuthenTraps.setDescription("Indicates whether the SNMP entity is permitted to\ngenerate authenticationFailure traps.  The value of this\nobject overrides any configuration information; as such,\nit provides a means whereby all authenticationFailure\ntraps may be disabled.\n\nNote that it is strongly recommended that this object\nbe stored in non-volatile memory so that it remains\nconstant across re-initializations of the network\nmanagement system.")
snmpSilentDrops = MibScalar((1, 3, 6, 1, 2, 1, 11, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpSilentDrops.setDescription("The total number of Confirmed Class PDUs (such as\nGetRequest-PDUs, GetNextRequest-PDUs,\nGetBulkRequest-PDUs, SetRequest-PDUs, and\nInformRequest-PDUs) delivered to the SNMP entity which\nwere silently dropped because the size of a reply\ncontaining an alternate Response Class PDU (such as a\nResponse-PDU) with an empty variable-bindings field\nwas greater than either a local constraint or the\nmaximum message size associated with the originator of\nthe request.")
snmpProxyDrops = MibScalar((1, 3, 6, 1, 2, 1, 11, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpProxyDrops.setDescription("The total number of Confirmed Class PDUs\n(such as GetRequest-PDUs, GetNextRequest-PDUs,\nGetBulkRequest-PDUs, SetRequest-PDUs, and\nInformRequest-PDUs) delivered to the SNMP entity which\nwere silently dropped because the transmission of\nthe (possibly translated) message to a proxy target\nfailed in a manner (other than a time-out) such that\nno Response Class PDU (such as a Response-PDU) could\nbe returned.")
snmpMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 1)).setRevisions(("2002-10-16 00:00","1995-11-09 00:00","1993-04-01 00:00",))
if mibBuilder.loadTexts: snmpMIB.setOrganization("IETF SNMPv3 Working Group")
if mibBuilder.loadTexts: snmpMIB.setContactInfo("WG-EMail:   snmpv3@lists.tislabs.com\nSubscribe:  snmpv3-request@lists.tislabs.com\n\nCo-Chair:   Russ Mundy\n            Network Associates Laboratories\npostal:     15204 Omega Drive, Suite 300\n            Rockville, MD 20850-4601\n            USA\nEMail:      mundy@tislabs.com\nphone:      +1 301 947-7107\n\nCo-Chair:   David Harrington\n            Enterasys Networks\npostal:     35 Industrial Way\n            P. O. Box 5005\n            Rochester, NH 03866-5005\n            USA\nEMail:      dbh@enterasys.com\nphone:      +1 603 337-2614\n\nEditor:     Randy Presuhn\n            BMC Software, Inc.\npostal:     2141 North First Street\n            San Jose, CA 95131\n            USA\nEMail:      randy_presuhn@bmc.com\nphone:      +1 408 546-1006")
if mibBuilder.loadTexts: snmpMIB.setDescription("The MIB module for SNMP entities.\n\nCopyright (C) The Internet Society (2002). This\nversion of this MIB module is part of RFC 3418;\nsee the RFC itself for full legal notices.")
snmpMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1))
snmpTrap = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1, 4))
snmpTrapOID = MibScalar((1, 3, 6, 1, 6, 3, 1, 1, 4, 1), ObjectIdentifier()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: snmpTrapOID.setDescription("The authoritative identification of the notification\ncurrently being sent.  This variable occurs as\nthe second varbind in every SNMPv2-Trap-PDU and\nInformRequest-PDU.")
snmpTrapEnterprise = MibScalar((1, 3, 6, 1, 6, 3, 1, 1, 4, 3), ObjectIdentifier()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: snmpTrapEnterprise.setDescription("The authoritative identification of the enterprise\nassociated with the trap currently being sent.  When an\nSNMP proxy agent is mapping an RFC1157 Trap-PDU\ninto a SNMPv2-Trap-PDU, this variable occurs as the\nlast varbind.")
snmpTraps = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1, 5))
snmpSet = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 1, 6))
snmpSetSerialNo = MibScalar((1, 3, 6, 1, 6, 3, 1, 1, 6, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpSetSerialNo.setDescription("An advisory lock used to allow several cooperating\ncommand generator applications to coordinate their\nuse of the SNMP set operation.\n\nThis object is used for coarse-grain coordination.\nTo achieve fine-grain coordination, one or more similar\nobjects might be defined within each MIB group, as\nappropriate.")
snmpMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 2))
snmpMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 2, 1))
snmpMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 1, 2, 2))

# Augmentions

# Notifications

coldStart = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 1)).setObjects(*() )
if mibBuilder.loadTexts: coldStart.setDescription("A coldStart trap signifies that the SNMP entity,\nsupporting a notification originator application, is\nreinitializing itself and that its configuration may\nhave been altered.")
warmStart = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 2)).setObjects(*() )
if mibBuilder.loadTexts: warmStart.setDescription("A warmStart trap signifies that the SNMP entity,\nsupporting a notification originator application,\nis reinitializing itself such that its configuration\nis unaltered.")
authenticationFailure = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 5)).setObjects(*() )
if mibBuilder.loadTexts: authenticationFailure.setDescription("An authenticationFailure trap signifies that the SNMP\nentity has received a protocol message that is not\nproperly authenticated.  While all implementations\nof SNMP entities MAY be capable of generating this\ntrap, the snmpEnableAuthenTraps object indicates\nwhether this trap will be generated.")

# Groups

snmpSetGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 5)).setObjects(*(("SNMPv2-MIB", "snmpSetSerialNo"), ) )
if mibBuilder.loadTexts: snmpSetGroup.setDescription("A collection of objects which allow several cooperating\ncommand generator applications to coordinate their\nuse of the set operation.")
systemGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 6)).setObjects(*(("SNMPv2-MIB", "sysName"), ("SNMPv2-MIB", "sysObjectID"), ("SNMPv2-MIB", "sysORID"), ("SNMPv2-MIB", "sysUpTime"), ("SNMPv2-MIB", "sysORDescr"), ("SNMPv2-MIB", "sysContact"), ("SNMPv2-MIB", "sysORLastChange"), ("SNMPv2-MIB", "sysLocation"), ("SNMPv2-MIB", "sysServices"), ("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysORUpTime"), ) )
if mibBuilder.loadTexts: systemGroup.setDescription("The system group defines objects which are common to all\nmanaged systems.")
snmpBasicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 7)).setObjects(*(("SNMPv2-MIB", "authenticationFailure"), ("SNMPv2-MIB", "coldStart"), ) )
if mibBuilder.loadTexts: snmpBasicNotificationsGroup.setDescription("The basic notifications implemented by an SNMP entity\nsupporting command responder applications.")
snmpGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 8)).setObjects(*(("SNMPv2-MIB", "snmpEnableAuthenTraps"), ("SNMPv2-MIB", "snmpSilentDrops"), ("SNMPv2-MIB", "snmpInASNParseErrs"), ("SNMPv2-MIB", "snmpInPkts"), ("SNMPv2-MIB", "snmpInBadVersions"), ("SNMPv2-MIB", "snmpProxyDrops"), ) )
if mibBuilder.loadTexts: snmpGroup.setDescription("A collection of objects providing basic instrumentation\nand control of an SNMP entity.")
snmpCommunityGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 9)).setObjects(*(("SNMPv2-MIB", "snmpInBadCommunityNames"), ("SNMPv2-MIB", "snmpInBadCommunityUses"), ) )
if mibBuilder.loadTexts: snmpCommunityGroup.setDescription("A collection of objects providing basic instrumentation\nof a SNMP entity which supports community-based\nauthentication.")
snmpObsoleteGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 10)).setObjects(*(("SNMPv2-MIB", "snmpOutNoSuchNames"), ("SNMPv2-MIB", "snmpInReadOnlys"), ("SNMPv2-MIB", "snmpInTotalReqVars"), ("SNMPv2-MIB", "snmpInSetRequests"), ("SNMPv2-MIB", "snmpOutGenErrs"), ("SNMPv2-MIB", "snmpOutGetRequests"), ("SNMPv2-MIB", "snmpOutPkts"), ("SNMPv2-MIB", "snmpOutBadValues"), ("SNMPv2-MIB", "snmpOutTraps"), ("SNMPv2-MIB", "snmpInNoSuchNames"), ("SNMPv2-MIB", "snmpInGetNexts"), ("SNMPv2-MIB", "snmpInGetRequests"), ("SNMPv2-MIB", "snmpOutGetResponses"), ("SNMPv2-MIB", "snmpInGenErrs"), ("SNMPv2-MIB", "snmpInTraps"), ("SNMPv2-MIB", "snmpInTotalSetVars"), ("SNMPv2-MIB", "snmpInGetResponses"), ("SNMPv2-MIB", "snmpOutSetRequests"), ("SNMPv2-MIB", "snmpInBadValues"), ("SNMPv2-MIB", "snmpInTooBigs"), ("SNMPv2-MIB", "snmpOutGetNexts"), ("SNMPv2-MIB", "snmpOutTooBigs"), ) )
if mibBuilder.loadTexts: snmpObsoleteGroup.setDescription("A collection of objects from RFC 1213 made obsolete\nby this MIB module.")
snmpWarmStartNotificationGroup = NotificationGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 11)).setObjects(*(("SNMPv2-MIB", "warmStart"), ) )
if mibBuilder.loadTexts: snmpWarmStartNotificationGroup.setDescription("An additional notification for an SNMP entity supporting\ncommand responder applications, if it is able to reinitialize\nitself such that its configuration is unaltered.")
snmpNotificationGroup = NotificationGroup((1, 3, 6, 1, 6, 3, 1, 2, 2, 12)).setObjects(*(("SNMPv2-MIB", "snmpTrapOID"), ("SNMPv2-MIB", "snmpTrapEnterprise"), ) )
if mibBuilder.loadTexts: snmpNotificationGroup.setDescription("These objects are required for entities\nwhich support notification originator applications.")

# Compliances

snmpBasicCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 1, 2, 1, 2)).setObjects(*(("SNMPv2-MIB", "snmpGroup"), ("SNMPv2-MIB", "systemGroup"), ("SNMPv2-MIB", "snmpBasicNotificationsGroup"), ("SNMPv2-MIB", "snmpSetGroup"), ("SNMPv2-MIB", "snmpCommunityGroup"), ) )
if mibBuilder.loadTexts: snmpBasicCompliance.setDescription("The compliance statement for SNMPv2 entities which\nimplement the SNMPv2 MIB.\n\nThis compliance statement is replaced by\nsnmpBasicComplianceRev2.")
snmpBasicComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 6, 3, 1, 2, 1, 3)).setObjects(*(("SNMPv2-MIB", "snmpGroup"), ("SNMPv2-MIB", "snmpWarmStartNotificationGroup"), ("SNMPv2-MIB", "snmpBasicNotificationsGroup"), ("SNMPv2-MIB", "snmpCommunityGroup"), ("SNMPv2-MIB", "systemGroup"), ("SNMPv2-MIB", "snmpSetGroup"), ) )
if mibBuilder.loadTexts: snmpBasicComplianceRev2.setDescription("The compliance statement for SNMP entities which\nimplement this MIB module.")

# Exports

# Module identity
mibBuilder.exportSymbols("SNMPv2-MIB", PYSNMP_MODULE_ID=snmpMIB)

# Objects
mibBuilder.exportSymbols("SNMPv2-MIB", system=system, sysDescr=sysDescr, sysObjectID=sysObjectID, sysUpTime=sysUpTime, sysContact=sysContact, sysName=sysName, sysLocation=sysLocation, sysServices=sysServices, sysORLastChange=sysORLastChange, sysORTable=sysORTable, sysOREntry=sysOREntry, sysORIndex=sysORIndex, sysORID=sysORID, sysORDescr=sysORDescr, sysORUpTime=sysORUpTime, snmp=snmp, snmpInPkts=snmpInPkts, snmpOutPkts=snmpOutPkts, snmpInBadVersions=snmpInBadVersions, snmpInBadCommunityNames=snmpInBadCommunityNames, snmpInBadCommunityUses=snmpInBadCommunityUses, snmpInASNParseErrs=snmpInASNParseErrs, snmpInTooBigs=snmpInTooBigs, snmpInNoSuchNames=snmpInNoSuchNames, snmpInBadValues=snmpInBadValues, snmpInReadOnlys=snmpInReadOnlys, snmpInGenErrs=snmpInGenErrs, snmpInTotalReqVars=snmpInTotalReqVars, snmpInTotalSetVars=snmpInTotalSetVars, snmpInGetRequests=snmpInGetRequests, snmpInGetNexts=snmpInGetNexts, snmpInSetRequests=snmpInSetRequests, snmpInGetResponses=snmpInGetResponses, snmpInTraps=snmpInTraps, snmpOutTooBigs=snmpOutTooBigs, snmpOutNoSuchNames=snmpOutNoSuchNames, snmpOutBadValues=snmpOutBadValues, snmpOutGenErrs=snmpOutGenErrs, snmpOutGetRequests=snmpOutGetRequests, snmpOutGetNexts=snmpOutGetNexts, snmpOutSetRequests=snmpOutSetRequests, snmpOutGetResponses=snmpOutGetResponses, snmpOutTraps=snmpOutTraps, snmpEnableAuthenTraps=snmpEnableAuthenTraps, snmpSilentDrops=snmpSilentDrops, snmpProxyDrops=snmpProxyDrops, snmpMIB=snmpMIB, snmpMIBObjects=snmpMIBObjects, snmpTrap=snmpTrap, snmpTrapOID=snmpTrapOID, snmpTrapEnterprise=snmpTrapEnterprise, snmpTraps=snmpTraps, snmpSet=snmpSet, snmpSetSerialNo=snmpSetSerialNo, snmpMIBConformance=snmpMIBConformance, snmpMIBCompliances=snmpMIBCompliances, snmpMIBGroups=snmpMIBGroups)

# Notifications
mibBuilder.exportSymbols("SNMPv2-MIB", coldStart=coldStart, warmStart=warmStart, authenticationFailure=authenticationFailure)

# Groups
mibBuilder.exportSymbols("SNMPv2-MIB", snmpSetGroup=snmpSetGroup, systemGroup=systemGroup, snmpBasicNotificationsGroup=snmpBasicNotificationsGroup, snmpGroup=snmpGroup, snmpCommunityGroup=snmpCommunityGroup, snmpObsoleteGroup=snmpObsoleteGroup, snmpWarmStartNotificationGroup=snmpWarmStartNotificationGroup, snmpNotificationGroup=snmpNotificationGroup)

# Compliances
mibBuilder.exportSymbols("SNMPv2-MIB", snmpBasicCompliance=snmpBasicCompliance, snmpBasicComplianceRev2=snmpBasicComplianceRev2)
