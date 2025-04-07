#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char *argv[]) {
    char buffer[5];
    char *acc = malloc(1);
    acc[0] = '\0';
    int fd = open("toto.txt", O_RDONLY);
    while(1){
        int n = read(fd, buffer, 4); // <- version C du read de Python
        if (n == 0) break;
        buffer[n] = '\0';
        acc = realloc(acc, strlen(acc) + n + 1);
        strcat(acc, buffer);
    }
    printf("%s\n", acc);
    free(acc);
    close(fd);
    return 0;
}
