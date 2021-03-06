USE [PLVTIProject]
GO
/****** Object:  StoredProcedure [dbo].[FactorSync]    Script Date: 12/15/2020 8:10:53 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		Arash&Avash
-- Create date: 1399/08/20
-- Description:	
-- =============================================
ALTER  PROCEDURE [dbo].[FactorSync] 

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	insert into [SPArticle]
([SPId],[MerchandiseId],[Amount],[UnitId],[UnitPrice],[AuxAmount],[SPADesc],[VTax],[VCharge],[Percentage],[FPId],[Id2],[ATotal],Merchandisename)
SELECT cast([SPId] as bigint)
      ,cast([MerchandiseId] as bigint)
      ,cast([Amount] as bigint)
      ,cast([UnitId] as bigint)
      ,cast([UnitPrice] as bigint)
      ,cast([AuxAmount] as bigint)
      ,[SPADesc]
      ,cast([VTax] as bigint)
      ,cast([VCharge] as bigint)
      ,cast([Percentage] as bigint)
      ,[FPId]
      ,Id
      ,cast([ATotal] as bigint)
	  ,(select top 1 name from [192.168.20.40].[goroohpakhsh].[dbo].__Merchandise__ where id=MerchandiseId)
  FROM [192.168.20.40].[goroohpakhsh].[dbo].__SPArticle__ a
  where 
  id not in (select id2 from SPArticle where spid=a.SPId ) and 
   isnumeric(a.[UnitPrice])=1 and  isnumeric(a.[AuxAmount])=1
  and  isnumeric(a.[VTax])=1 and   isnumeric(a.[VCharge])=1
  and   isnumeric(a.[ATotal])=1  and   isnumeric(a.[Percentage])=1

  ----------------------------------------
  delete from SPArticle  where id2 not in (select id from [192.168.20.40].[goroohpakhsh].[dbo].__SPArticle__ a where a.SPId=SPArticle.SPId )

  ---------------------------------------

  update b set
	   b.[SPId]			 =a.[SPId]
      ,b.[MerchandiseId] =a.[MerchandiseId]
      ,b.[Amount]		 =a.[Amount]
      ,b.[UnitId]		 =a.[UnitId]
      ,b.[UnitPrice]	 =a.[UnitPrice]
      ,b.[AuxAmount]	 =a.[AuxAmount]
      ,b.[SPADesc]		 =a.[SPADesc]
      ,b.[VTax]			 =a.[VTax]
      ,b.[VCharge]		 =a.[VCharge]
      ,b.[Percentage]	 =a.[Percentage]
      ,b.[FPId]			 =a.[FPId]
      ,b.Id2			 =a.Id
      ,b.[ATotal]		 =cast(a.[ATotal] as bigint)
	  ,b.Merchandisename =(select top 1 name from [192.168.20.40].[goroohpakhsh].[dbo].__Merchandise__ where id=a.MerchandiseId)
  FROM [192.168.20.40].[goroohpakhsh].[dbo].__SPArticle__ a
  join SPArticle b on a.Id=b.Id2 and a.SPId=b.SPId
  where isnumeric(a.[UnitPrice])=1 and  isnumeric(a.[AuxAmount])=1
  and  isnumeric(a.[VTax])=1 and   isnumeric(a.[VCharge])=1
  ----------------------------------------------------------------------
  
set identity_insert SPFactor on
insert into SPFactor
([id],[FactorNo],[ReferenceNo],[SPDate],[FactorType],[CustomerId],[Total],[Discount],[Expense],[SPDesc],[CustomerName],[CustomerPhoneNo],[CustomerEcCode],[CustomerAddress],[FPId],[SC],[FStatus],[FactorSubType],[Committed])
SELECT [id]
      ,[FactorNo]
      ,[ReferenceNo]
      ,[SPDate]
      ,
case
when FactorType=0 then 'خرید'
when FactorType=1 then 'فروش'
when FactorType=2 then 'برگشت از خريد'
when FactorType=3 then 'برگشت از فروش'
when FactorType=4 then 'پیش فاکتور'
when FactorType=7 then 'استعلام از خرید'
else 'نامشخص'
end as FactorType
      ,[CustomerId]
      ,[Total]
      ,[Discount]
      ,[Expense]
      ,[SPDesc]
      ,[CustomerName]
      ,[CustomerPhoneNo]
      ,[CustomerEcCode]
      ,[CustomerAddress]
      ,[FPId]
      ,[SC]
      ,[FStatus]
      ,[FactorSubType]
      ,[Committed]
  FROM [192.168.20.40].[goroohpakhsh].[dbo].__spfactor__
  where id not in (select id from SPFactor ) and [FactorType] in (0,1,2,3) and [CustomerId]>0
  set identity_insert SPFactor off


------------------------------

delete from SPFactor where id not in (select id FROM [192.168.20.40].[goroohpakhsh].[dbo].__spfactor__ where  [FactorType] in (0,1,2,3) and [CustomerId]>0)

------------------------------

update b set 			   	   
       b.[FactorNo]		   	=a.[FactorNo]		   
      ,b.[ReferenceNo]	   	=a.[ReferenceNo]	   
      ,b.[SPDate]		   	=a.[SPDate]		   
      ,b.[FactorType]	   	=(case
								when a.FactorType=0 then 'خرید'
								when a.FactorType=1 then 'فروش'
								when a.FactorType=2 then 'برگشت از خريد'
								when a.FactorType=3 then 'برگشت از فروش'
								when a.FactorType=4 then 'پیش فاکتور'
								when a.FactorType=7 then 'استعلام از خرید'
								else 'نامشخص'
							end	 )  
      ,b.[CustomerId]	   	=a.[CustomerId]	   
      ,b.[Total]			=cast(a.[Total] as bigint)			
      ,b.[Discount]		   	=cast(a.[Discount]	 as bigint)		   
      ,b.[Expense]		   	=cast(a.[Expense]	 as bigint)		   
      ,b.[SPDesc]		   	=a.[SPDesc]		   
      ,b.[CustomerName]	   	=a.[CustomerName]	   
      ,b.[CustomerPhoneNo]	=a.[CustomerPhoneNo]
      ,b.[CustomerEcCode] 	=a.[CustomerEcCode] 
      ,b.[CustomerAddress] 	=a.[CustomerAddress] 
      ,b.[FPId]			   	=a.[FPId]			   
      ,b.[SC]			   	=a.[SC]			   
      ,b.[FStatus]		   	=a.[FStatus]		   
      ,b.[FactorSubType]	=a.[FactorSubType]	
      ,b.[Committed]       	=a.[Committed]       
  FROM [192.168.20.40].[goroohpakhsh].[dbo].__spfactor__ a
  join spfactor b on a.id=b.id

END
