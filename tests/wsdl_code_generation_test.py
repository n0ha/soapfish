from __future__ import print_function

from nose import SkipTest

from pythonic_testcase import *

from soapfish import wsdl2py
from soapfish import xsd
from soapfish.testutil import generated_symbols

WSDL = b"""<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions
    xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:o2bsmsg="http://www.sk.o2.com/O2BS/Service/Base/1.0"
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
    xmlns:tns="http://new.webservice.namespace"
    xmlns:http="http://schemas.xmlsoap.org/wsdl/http/"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/"
    xmlns:msg="http://www.sk.o2.com/O2BS/Service/Provisioning/1.0"
    targetNamespace="http://new.webservice.namespace">

    <wsdl:import namespace="http://www.sk.o2.com/O2BS/Service/Provisioning/1.0" location="O2BS_ProvSrv.xsd"/>
    <wsdl:import namespace="http://www.sk.o2.com/O2BS/Service/Base/1.0" location="O2BS_Base.xsd"/>

    <wsdl:message name="ChangeServicesProvisioningRequest">
        <wsdl:part name="parameter" element="msg:ChangeServicesProvisioningRequest"/>
    </wsdl:message>
    <wsdl:message name="ChangeSubscriberStatusProvisioningRequest">
        <wsdl:part name="parameter" element="msg:ChangeSubscriberStatusProvisioningRequest"/>
    </wsdl:message>
    <wsdl:message name="ActivateSubscriberProvisioningRequest">
        <wsdl:part name="parameter" element="msg:ActivateSubscriberProvisioningRequest"/>
    </wsdl:message>
    <wsdl:message name="ChangeMSISDNAndSIMProvisioningRequest">
        <wsdl:part name="parameter" element="msg:ChangeMSISDNAndSIMProvisioningRequest"/>
    </wsdl:message>
    <wsdl:message name="SystemException">
        <wsdl:part name="parameter" element="o2bsmsg:SystemException"/>
    </wsdl:message>
    <wsdl:message name="ChangeServicesProvisioningResponse">
        <wsdl:part name="parameter" element="msg:ChangeServicesProvisioningResponse"/>
    </wsdl:message>
    <wsdl:message name="ChangeSubscriberStatusProvisioningResponse">
        <wsdl:part name="parameter" element="msg:ChangeSubscriberStatusProvisioningResponse"/>
    </wsdl:message>
    <wsdl:message name="ActivateSubscriberProvisioningResponse">
        <wsdl:part name="parameter" element="msg:ActivateSubscriberProvisioningResponse"/>
    </wsdl:message>
    <wsdl:message name="ChangeMSISDNAndSIMProvisioningResponse">
        <wsdl:part name="parameter" element="msg:ChangeMSISDNAndSIMProvisioningResponse"/>
    </wsdl:message>
    <wsdl:portType name="ProvisioningPortType">
        <wsdl:operation name="ChangeServices">
            <wsdl:input message="tns:ChangeServicesProvisioningRequest"/>
            <wsdl:output message="tns:ChangeServicesProvisioningResponse"/>
            <wsdl:fault name="fault1" message="tns:SystemException"/>
        </wsdl:operation>
        <wsdl:operation name="ChangeSubscriberStatus">
            <wsdl:input message="tns:ChangeSubscriberStatusProvisioningRequest"/>
            <wsdl:output message="tns:ChangeSubscriberStatusProvisioningResponse"/>
            <wsdl:fault name="fault1" message="tns:SystemException"/>
        </wsdl:operation>
        <wsdl:operation name="ActivateSubscriber">
            <wsdl:input message="tns:ActivateSubscriberProvisioningRequest"/>
            <wsdl:output message="tns:ActivateSubscriberProvisioningResponse"/>
            <wsdl:fault name="fault1" message="tns:SystemException"/>
        </wsdl:operation>
        <wsdl:operation name="ChangeMSISDNAndSIM">
            <wsdl:input message="tns:ChangeMSISDNAndSIMProvisioningRequest"/>
            <wsdl:output message="tns:ChangeMSISDNAndSIMProvisioningResponse"/>
            <wsdl:fault name="fault1" message="tns:SystemException"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="ProvisioningBinding" type="tns:ProvisioningPortType">
        <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="ChangeServices">
            <soap:operation soapAction="ChangeServices"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="fault1"/>
        </wsdl:operation>
        <wsdl:operation name="ChangeSubscriberStatus">
            <soap:operation soapAction="ChangeSubscriberStatus"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="fault1"/>
        </wsdl:operation>
        <wsdl:operation name="ActivateSubscriber">
            <soap:operation soapAction="ActivateSubscriber"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="fault1"/>
        </wsdl:operation>
        <wsdl:operation name="ChangeMSISDNAndSIM">
            <soap:operation soapAction="ChangeMSISDNAndSIM"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="fault1"/>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="ProvisioningService">
        <wsdl:port name="ProvisioningPort" binding="tns:ProvisioningBinding">
            <soap:address location="http://localhost:9696/O2BSProvisioning"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
"""

WSDL_HELLO = b"""<?xml version="1.0"?>
<wsdl:definitions xmlns:tns="http://flightdataservices.com/ops.wsdl" xmlns:xs="http://www.w3.org/2000/10/XMLSchema" xmlns:fds="http://flightdataservices.com/ops.xsd" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" name="OPS" targetNamespace="http://flightdataservices.com/ops.wsdl" xmlns="http://flightdataservices.com/ops.xsd">
	<wsdl:types>
		<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://flightdataservices.com/ops.xsd">
			<xs:complexType name="airport">
				<xs:sequence>
					<xs:element name="code_type">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:enumeration value="ICAO"/>
								<xs:enumeration value="IATA"/>
								<xs:enumeration value="FAA"/>
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<xs:element name="code" type="xs:string"/>
				</xs:sequence>
			</xs:complexType>

			<xs:complexType name="weight">
					<xs:sequence>
						<xs:element name="value" type="xs:integer"/>
						<xs:element name="unit">
							<xs:simpleType>
								<xs:restriction base="xs:string">
									<xs:enumeration value="kg"/>
									<xs:enumeration value="lb"/>
								</xs:restriction>
						</xs:simpleType>
						</xs:element>
					</xs:sequence>
			</xs:complexType>

			<xs:simpleType name="pilot">
				<xs:restriction base="xs:string">
					<xs:enumeration value="CAPTAIN"/>
					<xs:enumeration value="FIRST_OFFICER"/>
				</xs:restriction>
			</xs:simpleType>

			<xs:complexType name="ops">
				<xs:sequence>
					<xs:element name="aircraft" type="xs:string" nillable="false"/>
					<xs:element name="flight_number" type="xs:string"/>
					<xs:element name="type">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:enumeration value="COMMERCIAL"/>
								<xs:enumeration value="INCOMPLETE"/>
								<xs:enumeration value="ENGINE_RUN_UP"/>
								<xs:enumeration value="TEST"/>
								<xs:enumeration value="TRAINING"/>
								<xs:enumeration value="FERRY"/>
								<xs:enumeration value="POSITIONING"/>
								<xs:enumeration value="LINE_TRAINING"/>
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<xs:element name="takeoff_airport" type="fds:airport"/>
					<xs:element name="takeoff_gate_datetime" type="xs:dateTime" minOccurs="0"/>
					<xs:element name="takeoff_datetime" type="xs:dateTime"/>
					<xs:element name="takeoff_fuel" minOccurs="0" type="fds:weight"/>
					<xs:element name="takeoff_gross_weight" minOccurs="0" type="fds:weight"/>
					<xs:element name="takeoff_pilot" minOccurs="0" type="fds:pilot"/>
					<xs:element name="landing_airport" type="fds:airport"/>
					<xs:element name="landing_gate_datetime" type="xs:dateTime" minOccurs="0"/>
					<xs:element name="landing_datetime" type="xs:dateTime"/>
					<xs:element name="landing_fuel" minOccurs="0" type="fds:weight"/>
					<xs:element name="landing_pilot" minOccurs="0" type="fds:pilot"/>
					<xs:element name="destination_airport" minOccurs="0" type="fds:airport"/>
					<xs:element name="captain_code" minOccurs="0" type="xs:string"/>
					<xs:element name="first_officer_code" minOccurs="0" type="xs:string"/>
					<xs:element name="V2" minOccurs="0" type="xs:integer"/>
					<xs:element name="Vref" minOccurs="0" type="xs:integer"/>
					<xs:element name="Vapp" minOccurs="0" type="xs:integer"/>
				</xs:sequence>
			</xs:complexType>
			<xs:complexType name="status">
				<xs:sequence>
					<xs:element name="action">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:enumeration value="INSERTED"/>
								<xs:enumeration value="UPDATED"/>
								<xs:enumeration value="EXISTS"/>
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<xs:element name="id" type="xs:long"/>
				</xs:sequence>
			</xs:complexType>
			<xs:element name="ops" type="fds:ops"/>
			<xs:element name="status" type="fds:status"/>
		</xs:schema>
	</wsdl:types>
	<wsdl:message name="PutOpsInput">
		<wsdl:part name="body" element="fds:ops"/>
	</wsdl:message>
	<wsdl:message name="PutOpsOutput">
		<part name="body" element="fds:status"/>
	</wsdl:message>
	<wsdl:portType name="PutOpsPortType">
		<wsdl:operation name="PutOps">
			<wsdl:input message="tns:PutOpsInput"/>
			<wsdl:output message="tns:PutOpsOutput"/>
		</wsdl:operation>
	</wsdl:portType>
	<wsdl:binding name="PutOpsBinding" type="tns:PutOpsPortType">
		<soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
		<wsdl:operation name="PutOps">
			<soap:operation soapAction="http://polaris.flightdataservices.com/ws/ops/PutOps"/>
			<wsdl:input>
				<soap:body use="literal"/>
			</wsdl:input>
			<wsdl:output>
				<soap:body use="literal"/>
			</wsdl:output>
		</wsdl:operation>
	</wsdl:binding>
	<wsdl:service name="OPS">
		<wsdl:documentation>Register Flight Ops</wsdl:documentation>
		<wsdl:port name="PutOpsPort" binding="tns:PutOpsBinding">
			<soap:address location="http://polaris.flightdataservices.com/ws/ops"/>
		</wsdl:port>
	</wsdl:service>
</wsdl:definitions>
"""

WSDL_CHANGED = b"""<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions xmlns:o2bsmsg="http://www.sk.o2.com/O2BS/Service/Base/1.0"
                  xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:tns="http://new.webservice.namespace"
                  xmlns:http="http://schemas.xmlsoap.org/wsdl/http/"
                  xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
                  xmlns:msg="http://www.sk.o2.com/O2BS/Service/Provisioning/1.0"
                  targetNamespace="http://new.webservice.namespace">

    <wsdl:types>
        <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                    elementFormDefault="qualified" attributeFormDefault="unqualified"
                    targetNamespace="http://www.sk.o2.com/O2BS/Service/Provisioning/1.0"
                    xmlns:prov="http://www.sk.o2.com/O2BS/Service/Provisioning/1.0"
                    xmlns:o2bsmsg="http://www.sk.o2.com/O2BS/Service/Base/1.0"
                    xmlns:typ="http://www.sk.o2.com/O2BS/BE/BasicTypes/1.0"
                    xmlns:com="http://www.sk.o2.com/O2BS/BE/Common/1.0">

            <xsd:import namespace="http://www.sk.o2.com/O2BS/Service/Base/1.0" schemaLocation="/home/n0ha/code/eea/o2/documents/tibco-soap-interface/wsdl-changed/O2BS_Base.xsd"/>
            <xsd:import namespace="http://www.sk.o2.com/O2BS/BE/BasicTypes/1.0" schemaLocation="/home/n0ha/code/eea/o2/documents/tibco-soap-interface/wsdl-changed/O2BS_BasicTypes.xsd"/>
            <xsd:import namespace="http://www.sk.o2.com/O2BS/BE/Common/1.0" schemaLocation="/home/n0ha/code/eea/o2/documents/tibco-soap-interface/wsdl-changed/O2BS_Common.xsd"/>

            <xsd:complexType name="ActivateSubscriberProvisioningOrder">
                <xsd:complexContent>
                    <xsd:extension base="prov:ProvisioningOrder">
                        <xsd:sequence>
                            <xsd:element name="orderItem" type="prov:OrderItem" minOccurs="0" maxOccurs="unbounded"
                                         nillable="true"/>
                        </xsd:sequence>
                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>

            <xsd:complexType name="ChangeMSISDNAndSIMProvisioningOrder">
                <xsd:complexContent>
                    <xsd:extension base="prov:ProvisioningOrder">
                        <xsd:sequence>
                            <xsd:element name="newMSISDN" type="typ:msisdn" minOccurs="0" nillable="true"/>
                            <xsd:element name="newIMSI" type="typ:imsi" minOccurs="0" nillable="true"/>
                        </xsd:sequence>
                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>

            <xsd:complexType name="AttributeSpecificationKey">
                <xsd:complexContent>
                    <xsd:extension base="com:IDEntityKey">

                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>

            <xsd:complexType name="ChangeServicesProvisioningOrder">
                <xsd:complexContent>
                    <xsd:extension base="prov:ProvisioningOrder">
                        <xsd:sequence>
                            <xsd:element name="orderItem" type="prov:OrderItem" minOccurs="0" maxOccurs="unbounded"
                                         nillable="true"/>
                        </xsd:sequence>
                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>

            <xsd:complexType name="ChangeSubscriberStatusProvisioningOrder">
                <xsd:complexContent>
                    <xsd:extension base="prov:ProvisioningOrder">
                        <xsd:sequence>
                            <xsd:element name="action" nillable="true">
                                <xsd:simpleType>
                                    <xsd:restriction base="xsd:string">
                                        <xsd:enumeration value="reactivate"/>
                                        <xsd:enumeration value="suspend"/>
                                        <xsd:enumeration value="deactivate"/>
                                    </xsd:restriction>
                                </xsd:simpleType>
                            </xsd:element>
                        </xsd:sequence>
                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>

            <xsd:complexType name="OrderItem">
                <xsd:sequence>
                    <xsd:element name="itemId" type="com:IDEntityKey" nillable="true"/>
                    <xsd:element name="action" nillable="true">
                        <xsd:simpleType>
                            <xsd:restriction base="xsd:string">
                                <xsd:enumeration value="add"/>
                                <xsd:enumeration value="remove"/>
                            </xsd:restriction>
                        </xsd:simpleType>
                    </xsd:element>
                    <xsd:element name="product" type="prov:ProductSpecificationKey" minOccurs="0" nillable="true"/>
                    <xsd:element name="itemAtribute" type="prov:OrderItemAttribute" minOccurs="0" maxOccurs="unbounded"
                                 nillable="true"/>
                </xsd:sequence>
            </xsd:complexType>

            <xsd:complexType name="ProductSpecificationKey">
                <xsd:complexContent>
                    <xsd:extension base="com:IDEntityKey">
                        <xsd:sequence>
                            <xsd:element name="description" type="xsd:string" minOccurs="0" nillable="true"/>
                        </xsd:sequence>
                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>

            <xsd:complexType name="OrderItemAttribute">
                <xsd:sequence>
                    <xsd:element name="name" type="xsd:string" minOccurs="0" nillable="true"/>
                    <xsd:element name="value" type="xsd:string" minOccurs="0" nillable="true"/>
                    <xsd:element name="attributeSpecification" type="prov:AttributeSpecificationKey" minOccurs="0"
                                 nillable="true"/>
                </xsd:sequence>
            </xsd:complexType>

            <xsd:complexType name="ProvSubscriberKey">
                <xsd:sequence>
                    <xsd:element name="msisdn" type="typ:msisdn" minOccurs="0" nillable="true"/>
                    <xsd:element name="imsi" type="typ:imsi" minOccurs="0" nillable="true"/>
                </xsd:sequence>
            </xsd:complexType>

            <xsd:complexType name="ProvisioningOrder">
                <xsd:sequence>
                    <xsd:element name="subscriber" type="prov:ProvSubscriberKey" minOccurs="0" nillable="true"/>
                    <xsd:element name="orderId" type="com:IDEntityKey" minOccurs="0" nillable="true"/>
                </xsd:sequence>
            </xsd:complexType>

            <xsd:complexType name="ProvisioningRequestACK">
                <xsd:sequence>
                    <xsd:element name="status" nillable="true">
                        <xsd:simpleType>
                            <xsd:restriction base="xsd:string">
                                <xsd:enumeration value="success"/>
                            </xsd:restriction>
                        </xsd:simpleType>
                    </xsd:element>
                </xsd:sequence>
            </xsd:complexType>

            <xsd:complexType name="ProvisioningResponse">
                <xsd:complexContent>
                    <xsd:extension base="o2bsmsg:BaseResponse">
                        <xsd:sequence>
                            <xsd:annotation>
                                <xsd:documentation>
                                    Response for provisioning request.


                                </xsd:documentation>
                            </xsd:annotation>
                            <xsd:element name="status" nillable="true">
                                <xsd:annotation>
                                    <xsd:documentation>
                                        Status of request set by provisioning.
                                    </xsd:documentation>
                                </xsd:annotation>
                                <xsd:simpleType>
                                    <xsd:restriction base="xsd:string">
                                        <xsd:enumeration value="success"/>
                                    </xsd:restriction>
                                </xsd:simpleType>
                            </xsd:element>
                            <xsd:element name="responseTime" type="xsd:dateTime" minOccurs="0" nillable="true">
                                <xsd:annotation>
                                    <xsd:documentation>
                                        Time of finishing request by provisioning system.
                                    </xsd:documentation>
                                </xsd:annotation>
                            </xsd:element>
                        </xsd:sequence>
                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>
            <xsd:element name="ProvisioningResponse" type="prov:ProvisioningResponse"/>


            <xsd:element name="ChangeServicesProvisioningRequest">
                <xsd:complexType>
                    <xsd:complexContent>
                        <xsd:extension base="o2bsmsg:BaseRequest">
                            <xsd:sequence>
                                <xsd:element name="order" type="prov:ChangeServicesProvisioningOrder"/>
                            </xsd:sequence>
                        </xsd:extension>
                    </xsd:complexContent>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="ChangeServicesProvisioningResponse">
                <xsd:complexType>
                    <xsd:complexContent>
                        <xsd:extension base="o2bsmsg:BaseResponse">
                            <xsd:sequence>
                                <xsd:element name="value" type="prov:ProvisioningRequestACK"/>
                            </xsd:sequence>
                        </xsd:extension>
                    </xsd:complexContent>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="ChangeMSISDNAndSIMProvisioningRequest">
                <xsd:complexType>
                    <xsd:complexContent>
                        <xsd:extension base="o2bsmsg:BaseRequest">
                            <xsd:sequence>
                                <xsd:element name="order" type="prov:ChangeMSISDNAndSIMProvisioningOrder"/>
                            </xsd:sequence>
                        </xsd:extension>
                    </xsd:complexContent>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="ChangeMSISDNAndSIMProvisioningResponse">
                <xsd:complexType>
                    <xsd:complexContent>
                        <xsd:extension base="o2bsmsg:BaseResponse">
                            <xsd:sequence>
                                <xsd:element name="value" type="prov:ProvisioningRequestACK"/>
                            </xsd:sequence>
                        </xsd:extension>
                    </xsd:complexContent>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="ActivateSubscriberProvisioningRequest">
                <xsd:complexType>
                    <xsd:complexContent>
                        <xsd:extension base="o2bsmsg:BaseRequest">
                            <xsd:sequence>
                                <xsd:element name="order" type="prov:ActivateSubscriberProvisioningOrder"/>
                            </xsd:sequence>
                        </xsd:extension>
                    </xsd:complexContent>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="ActivateSubscriberProvisioningResponse">
                <xsd:complexType>
                    <xsd:complexContent>
                        <xsd:extension base="o2bsmsg:BaseResponse">
                            <xsd:sequence>
                                <xsd:element name="value" type="prov:ProvisioningRequestACK"/>
                            </xsd:sequence>
                        </xsd:extension>
                    </xsd:complexContent>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="ChangeSubscriberStatusProvisioningRequest">
                <xsd:complexType>
                    <xsd:complexContent>
                        <xsd:extension base="o2bsmsg:BaseRequest">
                            <xsd:sequence>
                                <xsd:element name="order" type="prov:ChangeSubscriberStatusProvisioningOrder"/>
                            </xsd:sequence>
                        </xsd:extension>
                    </xsd:complexContent>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="ChangeSubscriberStatusProvisioningResponse">
                <xsd:complexType>
                    <xsd:complexContent>
                        <xsd:extension base="o2bsmsg:BaseResponse">
                            <xsd:sequence>
                                <xsd:element name="value" type="prov:ProvisioningRequestACK"/>
                            </xsd:sequence>
                        </xsd:extension>
                    </xsd:complexContent>
                </xsd:complexType>
            </xsd:element>

        </xsd:schema>
<!--
        <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                    elementFormDefault="qualified" attributeFormDefault="unqualified"
                    targetNamespace="http://www.sk.o2.com/O2BS/Service/Base/1.0"
                    xmlns:o2bsmsg="http://www.sk.o2.com/O2BS/Service/Base/1.0">


            <xsd:complexType name="ApplicationException">
                <xsd:complexContent>
                    <xsd:extension base="o2bsmsg:BaseException">

                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>
            <xsd:element name="ApplicationException" type="o2bsmsg:ApplicationException"/>

            <xsd:complexType name="BaseException">
                <xsd:complexContent>
                    <xsd:extension base="o2bsmsg:BaseResponse">
                        <xsd:sequence>
                            <xsd:element name="code" type="xsd:string" nillable="true"/>
                            <xsd:element name="message" type="xsd:string" minOccurs="0" nillable="true"/>
                            <xsd:element name="source" type="xsd:string" minOccurs="0" nillable="true"/>
                            <xsd:element name="system" type="xsd:string" minOccurs="0" nillable="true"/>
                            <xsd:element name="stackTrace" type="xsd:string" minOccurs="0" nillable="true"/>
                            <xsd:element name="obj" type="xsd:string" minOccurs="0" nillable="true"/>
                        </xsd:sequence>
                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>

            <xsd:complexType name="BaseRequest" abstract="true">
                <xsd:complexContent>
                    <xsd:extension base="o2bsmsg:Message">
                        <xsd:sequence>
                            <xsd:element name="requestorDN" type="xsd:string" nillable="true"/>
                            <xsd:element name="userDN" type="xsd:string" minOccurs="0" nillable="true"/>
                        </xsd:sequence>
                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>

            <xsd:complexType name="BaseResponse" abstract="true">
                <xsd:complexContent>
                    <xsd:extension base="o2bsmsg:Message">
                        <xsd:sequence>
                            <xsd:element name="requestorDN" type="xsd:string" nillable="true"/>
                            <xsd:element name="correlationId" type="xsd:string" minOccurs="0" nillable="true"/>
                            <xsd:element name="processingReport" type="xsd:string" minOccurs="0" nillable="true"/>
                        </xsd:sequence>
                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>

            <xsd:complexType name="Message" abstract="true">
                <xsd:sequence>
                    <xsd:annotation>
                        <xsd:documentation>
                            Root message body. Body of all messages, which are sent on integration platform shall be
                            inherited from this class.

                        </xsd:documentation>
                    </xsd:annotation>
                    <xsd:element name="messageId" nillable="true">
                        <xsd:annotation>
                            <xsd:documentation>
                                System-wide unique identifier of message.
                            </xsd:documentation>
                        </xsd:annotation>
                        <xsd:simpleType>
                            <xsd:restriction base="xsd:string">
                                <xsd:pattern value="(\p{Lu})+::(\p{IsBasicLatin})+"/>
                            </xsd:restriction>
                        </xsd:simpleType>
                    </xsd:element>
                    <xsd:element name="timestamp" type="xsd:dateTime" minOccurs="0" nillable="true"/>
                </xsd:sequence>
            </xsd:complexType>

            <xsd:complexType name="ObjectNotFoundException">
                <xsd:complexContent>
                    <xsd:extension base="o2bsmsg:BaseException">

                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>
            <xsd:element name="ObjectNotFoundException" type="o2bsmsg:ObjectNotFoundException"/>

            <xsd:complexType name="SystemException">
                <xsd:complexContent>
                    <xsd:extension base="o2bsmsg:BaseException">

                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>
            <xsd:element name="SystemException" type="o2bsmsg:SystemException"/>

            <xsd:complexType name="BaseCommand">
                <xsd:complexContent>
                    <xsd:extension base="o2bsmsg:Message">
                        <xsd:sequence>
                            <xsd:element name="requestorDN" type="xsd:string" nillable="true">
                                <xsd:annotation>
                                    <xsd:documentation>
                                        Distinguished name of component, which sent the request. The list of
                                        distinguished names will be specified in [EAI-DP].
                                    </xsd:documentation>
                                </xsd:annotation>
                            </xsd:element>
                            <xsd:element name="userDN" type="xsd:string" minOccurs="0" nillable="true">
                                <xsd:annotation>
                                    <xsd:documentation>
                                        User, who performed the command.
                                    </xsd:documentation>
                                </xsd:annotation>
                            </xsd:element>
                        </xsd:sequence>
                    </xsd:extension>
                </xsd:complexContent>
            </xsd:complexType>

        </xsd:schema> -->
    </wsdl:types>

    <wsdl:message name="ChangeServicesProvisioningRequest">
        <wsdl:part name="parameter" element="msg:ChangeServicesProvisioningRequest"/>
    </wsdl:message>
    <wsdl:message name="ChangeSubscriberStatusProvisioningRequest">
        <wsdl:part name="parameter" element="msg:ChangeSubscriberStatusProvisioningRequest"/>
    </wsdl:message>
    <wsdl:message name="ActivateSubscriberProvisioningRequest">
        <wsdl:part name="parameter" element="msg:ActivateSubscriberProvisioningRequest"/>
    </wsdl:message>
    <wsdl:message name="ChangeMSISDNAndSIMProvisioningRequest">
        <wsdl:part name="parameter" element="msg:ChangeMSISDNAndSIMProvisioningRequest"/>
    </wsdl:message>
    <wsdl:message name="SystemException">
        <wsdl:part name="parameter" element="o2bsmsg:SystemException"/>
    </wsdl:message>
    <wsdl:message name="ChangeServicesProvisioningResponse">
        <wsdl:part name="parameter" element="msg:ChangeServicesProvisioningResponse"/>
    </wsdl:message>
    <wsdl:message name="ChangeSubscriberStatusProvisioningResponse">
        <wsdl:part name="parameter" element="msg:ChangeSubscriberStatusProvisioningResponse"/>
    </wsdl:message>
    <wsdl:message name="ActivateSubscriberProvisioningResponse">
        <wsdl:part name="parameter" element="msg:ActivateSubscriberProvisioningResponse"/>
    </wsdl:message>
    <wsdl:message name="ChangeMSISDNAndSIMProvisioningResponse">
        <wsdl:part name="parameter" element="msg:ChangeMSISDNAndSIMProvisioningResponse"/>
    </wsdl:message>
    <wsdl:portType name="ProvisioningPortType">
        <wsdl:operation name="ChangeServices">
            <wsdl:input message="tns:ChangeServicesProvisioningRequest"/>
            <wsdl:output message="tns:ChangeServicesProvisioningResponse"/>
            <wsdl:fault name="fault1" message="tns:SystemException"/>
        </wsdl:operation>
        <wsdl:operation name="ChangeSubscriberStatus">
            <wsdl:input message="tns:ChangeSubscriberStatusProvisioningRequest"/>
            <wsdl:output message="tns:ChangeSubscriberStatusProvisioningResponse"/>
            <wsdl:fault name="fault1" message="tns:SystemException"/>
        </wsdl:operation>
        <wsdl:operation name="ActivateSubscriber">
            <wsdl:input message="tns:ActivateSubscriberProvisioningRequest"/>
            <wsdl:output message="tns:ActivateSubscriberProvisioningResponse"/>
            <wsdl:fault name="fault1" message="tns:SystemException"/>
        </wsdl:operation>
        <wsdl:operation name="ChangeMSISDNAndSIM">
            <wsdl:input message="tns:ChangeMSISDNAndSIMProvisioningRequest"/>
            <wsdl:output message="tns:ChangeMSISDNAndSIMProvisioningResponse"/>
            <wsdl:fault name="fault1" message="tns:SystemException"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="ProvisioningBinding" type="tns:ProvisioningPortType">
        <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="ChangeServices">
            <soap:operation soapAction="ChangeServices"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="fault1"/>
        </wsdl:operation>
        <wsdl:operation name="ChangeSubscriberStatus">
            <soap:operation soapAction="ChangeSubscriberStatus"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="fault1"/>
        </wsdl:operation>
        <wsdl:operation name="ActivateSubscriber">
            <soap:operation soapAction="ActivateSubscriber"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="fault1"/>
        </wsdl:operation>
        <wsdl:operation name="ChangeMSISDNAndSIM">
            <soap:operation soapAction="ChangeMSISDNAndSIM"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="fault1"/>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="ProvisioningService">
        <wsdl:port name="ProvisioningPort" binding="tns:ProvisioningBinding">
            <soap:address location="http://localhost:9696/O2BSProvisioning"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
"""

class XSDCodeGenerationTest(PythonicTestCase):
    def test_can_generate_code_for_two_schemas(self):
        # raise SkipTest('can not generate code for wsdl with multiple schemas')
        xml = '<wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:b="http://example.org/B">' \
              '    <wsdl:types>' \
              '        <xsd:schema elementFormDefault="qualified" targetNamespace="http://example.org/A">' \
              '            <xsd:import namespace="http://example.org/B"/>' \
              '            <xsd:element name="A" type="b:B"/>' \
              '        </xsd:schema>' \
              '        <xsd:schema elementFormDefault="qualified" targetNamespace="http://example.org/B">' \
              '            <xsd:element name="B" type="xsd:string"/>' \
              '        </xsd:schema>' \
              '    </wsdl:types>' \
              '</wsdl:definitions>'
        code_string = wsdl2py.generate_code_from_wsdl(xml, 'client')

        schema, new_symbols = generated_symbols(code_string)
        assert_not_none(schema)
        assert_length(4, new_symbols)

        assert_equals(['B', 'A'], list(schema.elements))

    def test_can_generate_code_for_hello(self):
        code_string = wsdl2py.generate_code_from_wsdl(WSDL_CHANGED, 'client')

        schema, new_symbols = generated_symbols(code_string)
        assert_not_none(schema)
        # assert_length(4, new_symbols)

    def test_can_generate_code_for_multiple_schemas(self):
        # raise SkipTest('can not generate code for wsdl with multiple schemas')
        code_string = wsdl2py.generate_code_from_wsdl(WSDL, 'client')

        schema, new_symbols = generated_symbols(code_string)
        assert_not_none(schema)
        assert_length(4, new_symbols)

        assert_equals(['B', 'A'], list(schema.elements))

    def test_can_generate_code_for_inheritance(self):
        raise SkipTest('can not generate code for wsdl with type inheritance')
        xml = '<wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:xsd="http://www.w3.org/2001/XMLSchema">' \
              '    <wsdl:types>' \
              '        <xsd:schema elementFormDefault="qualified" targetNamespace="http://example.org/A">' \
              '            <xsd:element name="A" type="B"/>' \
              '            <xsd:element name="B" type="xsd:string"/>' \
              '        </xsd:schema>' \
              '    </wsdl:types>' \
              '</wsdl:definitions>'
        code_string = wsdl2py.generate_code_from_wsdl(xml, 'client')

        schema, new_symbols = generated_symbols(code_string)
        assert_not_none(schema)
        assert_length(4, new_symbols)

        assert_equals(['B', 'A'], list(schema.elements))
        assert_isinstance(schema.elements['B']._type, xsd.String)
        assert_isinstance(schema.elements['A']._type, schema.elements['B']._type.__class__)
