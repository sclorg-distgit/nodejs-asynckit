%{?scl:%scl_package nodejs-asynckit}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name asynckit

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    0.4.0
Release:    1%{?dist}
Summary:    Minimal async jobs utility library, with streams support
License:    MIT
URL:        https://github.com/alexindigo/asynckit#readme
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Minimal async jobs utility library, with streams support

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr bench.js index.js lib package.json parallel.js serial.js serialOrdered.js stream.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Mon Jan 16 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.4.0-1
- Initial build

