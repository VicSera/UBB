USE [ClimbingDB]
GO
ALTER TABLE [dbo].[region] DROP CONSTRAINT [FK__region__country___76969D2E]
GO
ALTER TABLE [dbo].[region] DROP CONSTRAINT [FK__region__country___5AEE82B9]
GO
ALTER TABLE [dbo].[region] DROP CONSTRAINT [FK__region__country___498EEC8D]
GO
ALTER TABLE [dbo].[region] DROP CONSTRAINT [FK__region__country___3F466844]
GO
ALTER TABLE [dbo].[region] DROP CONSTRAINT [FK__region__country___2DE6D218]
GO
ALTER TABLE [dbo].[region] DROP CONSTRAINT [FK__region__country___123EB7A3]
GO
ALTER TABLE [dbo].[outdoorEvent] DROP CONSTRAINT [FK__outdoorEv__crag___7E37BEF6]
GO
ALTER TABLE [dbo].[outdoorEvent] DROP CONSTRAINT [FK__outdoorEv__crag___628FA481]
GO
ALTER TABLE [dbo].[outdoorEvent] DROP CONSTRAINT [FK__outdoorEv__crag___51300E55]
GO
ALTER TABLE [dbo].[outdoorEvent] DROP CONSTRAINT [FK__outdoorEv__crag___46E78A0C]
GO
ALTER TABLE [dbo].[outdoorEvent] DROP CONSTRAINT [FK__outdoorEv__crag___3587F3E0]
GO
ALTER TABLE [dbo].[outdoorEvent] DROP CONSTRAINT [FK__outdoorEv__crag___19DFD96B]
GO
ALTER TABLE [dbo].[indoorEvent] DROP CONSTRAINT [FK__indoorEve__gym_i__7D439ABD]
GO
ALTER TABLE [dbo].[indoorEvent] DROP CONSTRAINT [FK__indoorEve__gym_i__619B8048]
GO
ALTER TABLE [dbo].[indoorEvent] DROP CONSTRAINT [FK__indoorEve__gym_i__503BEA1C]
GO
ALTER TABLE [dbo].[indoorEvent] DROP CONSTRAINT [FK__indoorEve__gym_i__45F365D3]
GO
ALTER TABLE [dbo].[indoorEvent] DROP CONSTRAINT [FK__indoorEve__gym_i__3493CFA7]
GO
ALTER TABLE [dbo].[indoorEvent] DROP CONSTRAINT [FK__indoorEve__gym_i__18EBB532]
GO
ALTER TABLE [dbo].[gym] DROP CONSTRAINT [FK__gym__city_code__797309D9]
GO
ALTER TABLE [dbo].[gym] DROP CONSTRAINT [FK__gym__city_code__5DCAEF64]
GO
ALTER TABLE [dbo].[gym] DROP CONSTRAINT [FK__gym__city_code__4C6B5938]
GO
ALTER TABLE [dbo].[gym] DROP CONSTRAINT [FK__gym__city_code__4222D4EF]
GO
ALTER TABLE [dbo].[gym] DROP CONSTRAINT [FK__gym__city_code__30C33EC3]
GO
ALTER TABLE [dbo].[gym] DROP CONSTRAINT [FK__gym__city_code__151B244E]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__74AE54BC]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__73BA3083]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__59063A47]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__5812160E]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__47A6A41B]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__46B27FE2]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__3C69FB99]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__3B75D760]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__2BFE89A6]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__2B0A656D]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__10566F31]
GO
ALTER TABLE [dbo].[friendship] DROP CONSTRAINT [FK__friendshi__climb__0F624AF8]
GO
ALTER TABLE [dbo].[crag] DROP CONSTRAINT [FK__crag__region_cod__787EE5A0]
GO
ALTER TABLE [dbo].[crag] DROP CONSTRAINT [FK__crag__region_cod__5CD6CB2B]
GO
ALTER TABLE [dbo].[crag] DROP CONSTRAINT [FK__crag__region_cod__4B7734FF]
GO
ALTER TABLE [dbo].[crag] DROP CONSTRAINT [FK__crag__region_cod__412EB0B6]
GO
ALTER TABLE [dbo].[crag] DROP CONSTRAINT [FK__crag__region_cod__2FCF1A8A]
GO
ALTER TABLE [dbo].[crag] DROP CONSTRAINT [FK__crag__region_cod__14270015]
GO
ALTER TABLE [dbo].[climbingRoute] DROP CONSTRAINT [FK__climbingR__crag___7A672E12]
GO
ALTER TABLE [dbo].[climbingRoute] DROP CONSTRAINT [FK__climbingR__crag___5EBF139D]
GO
ALTER TABLE [dbo].[climbingRoute] DROP CONSTRAINT [FK__climbingR__crag___4D5F7D71]
GO
ALTER TABLE [dbo].[climbingRoute] DROP CONSTRAINT [FK__climbingR__crag___4316F928]
GO
ALTER TABLE [dbo].[climbingRoute] DROP CONSTRAINT [FK__climbingR__crag___31B762FC]
GO
ALTER TABLE [dbo].[climbingRoute] DROP CONSTRAINT [FK__climbingR__crag___160F4887]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__event__66603565]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__event__55009F39]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__event__4AB81AF0]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__event__395884C4]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__event__1DB06A4F]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__event__02084FDA]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__climb__656C112C]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__climb__540C7B00]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__climb__49C3F6B7]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__climb__3864608B]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__climb__1CBC4616]
GO
ALTER TABLE [dbo].[climber_outdoorEvent] DROP CONSTRAINT [FK__climber_o__climb__01142BA1]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__event__6477ECF3]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__event__531856C7]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__event__48CFD27E]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__event__37703C52]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__event__1BC821DD]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__event__00200768]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__climb__7F2BE32F]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__climb__6383C8BA]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__climb__5224328E]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__climb__47DBAE45]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__climb__367C1819]
GO
ALTER TABLE [dbo].[climber_indoorEvent] DROP CONSTRAINT [FK__climber_i__climb__1AD3FDA4]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__7C4F7684]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__7B5B524B]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__60A75C0F]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__5FB337D6]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__4F47C5E3]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__4E53A1AA]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__44FF419A]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__440B1D61]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__339FAB6E]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__32AB8735]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__17F790F9]
GO
ALTER TABLE [dbo].[climber_climbingRoute] DROP CONSTRAINT [FK__climber_c__climb__17036CC0]
GO
ALTER TABLE [dbo].[climber] DROP CONSTRAINT [FK__climber__gym_id__75A278F5]
GO
ALTER TABLE [dbo].[climber] DROP CONSTRAINT [FK__climber__gym_id__59FA5E80]
GO
ALTER TABLE [dbo].[climber] DROP CONSTRAINT [FK__climber__gym_id__489AC854]
GO
ALTER TABLE [dbo].[climber] DROP CONSTRAINT [FK__climber__gym_id__3E52440B]
GO
ALTER TABLE [dbo].[climber] DROP CONSTRAINT [FK__climber__gym_id__2CF2ADDF]
GO
ALTER TABLE [dbo].[climber] DROP CONSTRAINT [FK__climber__gym_id__114A936A]
GO
ALTER TABLE [dbo].[city] DROP CONSTRAINT [FK__city__region_cod__778AC167]
GO
ALTER TABLE [dbo].[city] DROP CONSTRAINT [FK__city__region_cod__5BE2A6F2]
GO
ALTER TABLE [dbo].[city] DROP CONSTRAINT [FK__city__region_cod__4A8310C6]
GO
ALTER TABLE [dbo].[city] DROP CONSTRAINT [FK__city__region_cod__403A8C7D]
GO
ALTER TABLE [dbo].[city] DROP CONSTRAINT [FK__city__region_cod__2EDAF651]
GO
ALTER TABLE [dbo].[city] DROP CONSTRAINT [FK__city__region_cod__1332DBDC]
GO
/****** Object:  Table [dbo].[region]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[region]') AND type in (N'U'))
DROP TABLE [dbo].[region]
GO
/****** Object:  Table [dbo].[outdoorEvent]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[outdoorEvent]') AND type in (N'U'))
DROP TABLE [dbo].[outdoorEvent]
GO
/****** Object:  Table [dbo].[indoorEvent]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[indoorEvent]') AND type in (N'U'))
DROP TABLE [dbo].[indoorEvent]
GO
/****** Object:  Table [dbo].[gym]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[gym]') AND type in (N'U'))
DROP TABLE [dbo].[gym]
GO
/****** Object:  Table [dbo].[friendship]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[friendship]') AND type in (N'U'))
DROP TABLE [dbo].[friendship]
GO
/****** Object:  Table [dbo].[crag]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[crag]') AND type in (N'U'))
DROP TABLE [dbo].[crag]
GO
/****** Object:  Table [dbo].[country]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[country]') AND type in (N'U'))
DROP TABLE [dbo].[country]
GO
/****** Object:  Table [dbo].[climbingRoute]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[climbingRoute]') AND type in (N'U'))
DROP TABLE [dbo].[climbingRoute]
GO
/****** Object:  Table [dbo].[climber_outdoorEvent]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[climber_outdoorEvent]') AND type in (N'U'))
DROP TABLE [dbo].[climber_outdoorEvent]
GO
/****** Object:  Table [dbo].[climber_indoorEvent]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[climber_indoorEvent]') AND type in (N'U'))
DROP TABLE [dbo].[climber_indoorEvent]
GO
/****** Object:  Table [dbo].[climber_climbingRoute]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[climber_climbingRoute]') AND type in (N'U'))
DROP TABLE [dbo].[climber_climbingRoute]
GO
/****** Object:  Table [dbo].[climber]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[climber]') AND type in (N'U'))
DROP TABLE [dbo].[climber]
GO
/****** Object:  Table [dbo].[city]    Script Date: 10/22/2020 11:39:24 AM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[city]') AND type in (N'U'))
DROP TABLE [dbo].[city]
GO
