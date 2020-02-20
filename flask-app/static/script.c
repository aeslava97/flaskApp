#include <mysql/mysql.h>
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h> 
	

int main(int argc, char *argv[]) {
   bool encontrado=true;
   MYSQL *conn;
	MYSQL_RES *res;
	MYSQL_ROW row;
	 
	char *server = "mysql";
	char *user = "root";
	char *password = "root"; /* set me first */
	char *database = "test";

 
	conn = mysql_init(NULL);
	
	/* Connect to database */
	if (!mysql_real_connect(conn, server, user, password, 
                                      database, 0, NULL, 0)) {
		fprintf(stderr, "%s\n", mysql_error(conn));
		exit(1);
	}
	
	/* send SQL query */
	if (mysql_query(conn,"SELECT  * FROM CuponValido")) {
		fprintf(stderr, "%s\n", mysql_error(conn));
		exit(1);
	}
   
	res = mysql_use_result(conn);
	
	/* output table name */
	
	
   
    while ((row = mysql_fetch_row(res)) != NULL)
    {
printf("%s",row[0]);
       
   int res =strcmp(row[0], argv[1]);
       if(res == 0 )
       {  

          printf("%s",row[1]);
          return 0;
       }  
       
    }
    
         printf("%d",0);
          return 1;

         

	/* close connection */
	mysql_free_result(res);
	mysql_close(conn);

     }