USE [PLVTIProject]
GO
/****** Object:  StoredProcedure [dbo].[PayRcvSync]    Script Date: 12/19/2020 11:00:59 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		Arash&Avash
-- Create date: 1399/09/18
-- Description:	
-- =============================================
ALTER  PROCEDURE [dbo].[PayRcvSync] 

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	insert into [dbo].[PayRcvCheck]
		([CheckId],[PayRcvId])
	SELECT [CheckId]
      ,[PayRcvId]
	FROM [192.168.20.40].[goroohpakhsh].[dbo].__PayRcvCheck__ a
	where 
	CheckId not in (select CheckId from [dbo].[PayRcvCheck] where CheckId=a.CheckId and PayRcvId=a.PayRcvId )
  ----------------------------------------
  delete from [dbo].[PayRcvCheck] where CheckId not in (select CheckId from [192.168.20.40].[goroohpakhsh].[dbo].__PayRcvCheck__ a where a.CheckId=[dbo].[PayRcvCheck].CheckId )

  ---------------------------------------

	insert into [dbo].[Check]
	([id2],[CheckNo],[CValue],[PayerFAccId],[CDate],[RcptDate],[VDate],[CStatus],[CType],[SType],[CId])
	SELECT [id]
		  ,[CheckNo]
		  ,[CValue]
		  ,[PayerFAccId]
		  ,[CDate]
		  ,[RcptDate]
		  ,[VDate]
		  ,[CStatus]
		  ,[CType]
		  ,[SType]
		  ,[CId]
	  FROM [192.168.20.40].[goroohpakhsh].[dbo].__Check__ a
	  where 
	  id not in (select id2 from [dbo].[Check] where id2=a.id )

  ----------------------------------------
  delete from [dbo].[Check]  where id2 not in (select id from [192.168.20.40].[goroohpakhsh].[dbo].__Check__ a where a.id=[dbo].[Check].id2 )
  ---------------------------------------

  update b set
	   b.[id2]			 =a.[id]
      ,b.[CheckNo] =a.[CheckNo]
      ,b.[CValue]		 =cast(a.[CValue] as bigint)
      ,b.[PayerFAccId]		 =a.[PayerFAccId]
      ,b.[CDate]	 =dbo.__MiladiToShamsi__(a.[CDate])
      ,b.[RcptDate]	 =dbo.__MiladiToShamsi__(a.[RcptDate])
      ,b.[VDate]		 =a.[VDate]
      ,b.[CStatus]			 =(select Name from [192.168.20.40].[goroohpakhsh].[dbo].__AccParam__ where ParentId=4 and id=a.[CStatus])
      ,b.[CType]		 =a.[CType]
      ,b.[SType]	 =(select Name from [192.168.20.40].[goroohpakhsh].[dbo].__AccParam__ where ParentId=5 and id=a.[SType])
	  ,b.[CId]     = a.[CId]
  FROM [192.168.20.40].[goroohpakhsh].[dbo].__Check__ a
  join [dbo].[Check] b on a.Id=b.Id2 and a.CheckNo=b.CheckNo
  ----------------------------------------------------------------------
  
set identity_insert [dbo].[PayRcv] on
insert into [dbo].[PayRcv]
([id],[PNo],[PayType],[PDate],[RcvrFAccId],[PDesc],[CustomerId],[PCValue],[SCommit])
SELECT [id]
      ,[PNo]
      ,(select Name from [192.168.20.40].[goroohpakhsh].[dbo].__AccParam__ where ParentId=8 and id=[PayType]) as PayType
      ,[PDate]
      ,[RcvrFAccId]
      ,[PDesc]
      ,[CustomerId]
      ,[PCValue]
	  ,[SCommit]
  FROM [192.168.20.40].[goroohpakhsh].[dbo].__PayRcv__
  where id not in (select id from [dbo].[PayRcv]) and [PayType]>0
  set identity_insert [dbo].[PayRcv] off
------------------------------
delete from [dbo].[PayRcv] where id not in (select id FROM [192.168.20.40].[goroohpakhsh].[dbo].__PayRcv__ where  [PayType]>0)
------------------------------
update b set 			   	   
       b.[PNo]				= a.PNo		   
      ,b.[PayType]			= (select Name from [192.168.20.40].[goroohpakhsh].[dbo].__AccParam__ where ParentId=8 and id=a.PayType)	   
      ,b.[PDate]		   	= a.[PDate]		   
      ,b.[RcvrFAccId]	   	= (select top 1 Name from [192.168.20.40].[goroohpakhsh].[dbo].__Customer__ where FAccId=a.RcvrFAccId)	
      ,b.[PDesc]	   		= a.[PDesc]	   
      ,b.[CustomerId]		= a.[CustomerId]--(select Name from [192.168.20.40].[goroohpakhsh].[dbo].__Customer__ where FAccId=a.CustomerId)	
      ,b.[PCValue]	   		= cast(a.PCValue as bigint)		          
	  ,b.[SCommit]          = a.[SCommit]
  FROM [192.168.20.40].[goroohpakhsh].[dbo].__PayRcv__ a
  join [dbo].[PayRcv] b on a.id=b.id

 -- update for pcvalue where pcvalue = 0 in payrcv and cvalue <> 0 in check
begin
with tmp as(
select a.PCValue,isnull((select sum(cast(c.CValue as bigint))  from  [Check] c where c.Id2 in 
(select b.CheckId from  PayRcvCheck b where b.PayRcvId=a.id  ) and c.cvalue<>'0' ), 0) as sss from PayRcv a
where  a.PCValue<>isnull((select sum(cast(c.CValue as bigint))   from  [Check] c where c.Id2 in 
(select b.CheckId from  PayRcvCheck b where b.PayRcvId=a.id  ) and c.cvalue<>'0' ), 0) )
update tmp set PCValue=sss
end

END

