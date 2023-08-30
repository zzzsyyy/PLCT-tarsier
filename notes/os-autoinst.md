https://github.com/os-autoinst/os-autoinst

## `test_flag`

> 'fatal' - abort whole test suite if this fails (and set overall state 'failed')
>
> 'ignore_failure' - if this module fails, it will not affect the overall result at all
>
> 'milestone' - after this test succeeds, update 'lastgood'
>
> 'no_rollback' - don't roll back to 'lastgood' snapshot if this fails
>
> 'always_rollback' - roll back to 'lastgood' snapshot even if test was successful (supported on QEMU backend only)


```perl
 sub test_flags {
     return {fatal => 1, milestone=>1};
 }
```

## `wait_serial` no die

```perl
# should use
wait_serial(xxx, timeout=>x) || die "die msg";
```
