## use sub func in other file

in `file1.pm` use functions in `file2.pm`

```perl
package xxx

use Exporter 'import';
our @EXPORT = qw(fun1 fun2);

sub fun1 {
    #xxx
}

sub fun2 {
    #xxx
}

1;
```
