Summary: Valgrind Memory Debugger
Name: valgrind
Version: 1.0.4
Release: 1
Copyright: GPL
Group: Development/Debuggers
Packager: Frederic Gobry  <frederic.gobry@smartdata.ch>
Source: valgrind-1.0.4.tar.bz2

Buildroot: %{_tmppath}/valgrind

%description 

Valgrind is a GPL'd tool to help you find memory-management problems
in your programs. When a program is run under Valgrind's supervision,
all reads and writes of memory are checked, and calls to
malloc/new/free/delete are intercepted. As a result, Valgrind can
detect problems such as:

- Use of uninitialised memory 
- Reading/writing memory after it has been free'd 
- Reading/writing off the end of malloc'd blocks 
- Reading/writing inappropriate areas on the stack 
- Memory leaks -- where pointers to malloc'd blocks are lost forever
- Passing of uninitialised and/or unaddressible memory to system calls
- Mismatched use of malloc/new/new [] vs free/delete/delete []
- Some abuses of the POSIX Pthreads API

%prep
%setup -n valgrind-1.0.4

%build
./configure --prefix=/usr
make

%install
make install prefix=$RPM_BUILD_ROOT/usr

%files
%defattr(-,root,root)
/usr/include/valgrind.h
/usr/bin/valgrind
/usr/bin/cachegrind
/usr/bin/vg_annotate
/usr/lib/valgrind/*

%doc
/usr/share/doc/valgrind/*

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf ${RPM_BUILD_ROOT}
