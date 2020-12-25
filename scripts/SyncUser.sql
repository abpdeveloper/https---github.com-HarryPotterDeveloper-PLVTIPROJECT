USE [PLVTIProject]
GO

/****** Object:  StoredProcedure [dbo].[SyncUser]    Script Date: 21/08/1399 01:47:33 ق.ظ ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		Arash&Avash
-- Create date: 1399/08/19
-- Description:	
-- =============================================
CREATE OR ALTER PROCEDURE [dbo].[SyncUser] 
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	 
INSERT INTO [dbo].[auth_user]
           ([password]
           ,[last_login]
           ,[is_superuser]
           ,[username]
           ,[first_name]
           ,[last_name]
           ,[email]
           ,[is_staff]
           ,[is_active]
           ,[date_joined]
           ,[avatar]
           ,[cellphone]
           ,[newpass]
           ,[oldpassword]
           ,[customersid_id])
     select 
           'pbkdf2_sha256$180000$28kafuPNDQhl$cnH1x5IStqcdZvkLf6oLiCU1u962/0viXBn1Ha4ay0A='
           ,GETDATE()
           ,0
           ,a.TRes
           ,a.Name
           ,a.Family
           ,a.Email
           ,1
           ,1
           ,GETDATE()
           ,Null
           ,a.CellPhone
           ,Null
           ,Null
           ,a.id
	from Customers a
	where len(a.TRes)=10
	and a.id not in (select[customersid_id] from auth_user )

END
GO


