USE PLVTIProject
GO

/****** Object:  UserDefinedFunction [dbo].[__MiladiToShamsi__]    Script Date: 22/08/1399 11:56:33 ق.ظ ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE  or alter FUNCTION [dbo].[__MiladiToShamsi__](@pMldDate DateTime) RETURNS NVARCHAR(10) AS BEGIN DECLARE @Sh_Y INT, @Sh_M INT, @Sh_D INT, @TmpY INT, @Leap INT, @Result INT, @stSD char(2), @stSM char(2),@Final nchar(10) if @pMldDate IS NULL RETURN '' Set @Result = convert(INT, convert(float,@pMldDate)) if @Result <= 78 BEGIN Set @Sh_Y = 1278 Set @Sh_M = (@Result + 10) / 30 + 10 Set @Sh_D = (@Result + 10) % 30 + 1 END ELSE BEGIN Set @Result = @Result - 78 Set @Sh_Y = 1279 while 1 = 1 BEGIN 	Set @TmpY = @Sh_Y + 11 	Set @TmpY = @TmpY - ( @TmpY / 33) * 33 	IF  (@TmpY <> 32) and ( (@TmpY / 4) * 4 = @TmpY ) 	Set @Leap = 1 	ELSE 	Set @Leap = 0 	IF @Result <= (365+@Leap) 	break 	Set @Result = @Result -  (365+@Leap) 	Set @Sh_Y = @Sh_Y + 1 END IF @Result <= 31*6 BEGIN 	Set @Sh_M = (@Result-1) / 31 + 1 	Set @Sh_D = (@Result-1) % 31 + 1 END ELSE  BEGIN 	Set @Sh_M = ((@Result-1) - 31*6) / 30 + 7 	Set @Sh_D = ((@Result-1) - 31*6) % 30 + 1 END END Set @stSM = ltrim(str(@Sh_M)) Set @stSD = ltrim(str(@Sh_D)) if Len(@stSD) < 2 Set @stSD= '0' + @stSD if Len(@stSM) < 2  Set @stSM= '0' + @stSM  Set @Final = ltrim(str(@SH_Y))+ '/' + @stSM + '/' +@stSD RETURN @Final END 
GO


