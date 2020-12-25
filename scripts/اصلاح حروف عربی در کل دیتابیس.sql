
 
 DECLARE @Table NVARCHAR(MAX),  
        @Col NVARCHAR(MAX)  
   
 DECLARE Table_Cursor CURSOR   
 FOR  
    --ÅÌœ« ﬂ—œ‰  „«„ ›Ì·œÂ«Ì „ ‰Ì  „«„ Ãœ«Ê· œÌ «»Ì” Ã«—Ì  
    SELECT a.name, --table  
           b.name --col  
    FROM   sysobjects a,  
           syscolumns b  
    WHERE  a.id = b.id  
           AND a.xtype = 'u' --User table  
           AND (  
                   b.xtype = 99 --ntext  
                   OR b.xtype = 35 -- text  
                   OR b.xtype = 231 --nvarchar  
                   OR b.xtype = 167 --varchar  
                   OR b.xtype = 175 --char  
                   OR b.xtype = 239 --nchar  
               )  
   
 OPEN Table_Cursor FETCH NEXT FROM  Table_Cursor INTO @Table,@Col  
 WHILE (@@FETCH_STATUS = 0)  
 BEGIN  
   EXEC (  
            'update [' + @Table + '] set [' + @Col +  
            ']= REPLACE(REPLACE(CAST([' + @Col +  
            '] as nvarchar(max)) , NCHAR(1740), NCHAR(1610)),NCHAR(1705),NCHAR(1603)) '  
        )   
    PRINT 'Table: ' + @Table +' Col: '+ @Col;
    FETCH NEXT FROM Table_Cursor INTO @Table,@Col  
 END CLOSE Table_Cursor DEALLOCATE Table_Cursor 
