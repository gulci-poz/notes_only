FROM microsoft/aspnetcore-build

MAINTAINER gulci

COPY . /app

WORKDIR /app

RUN bower install --allow-root

RUN dotnet restore

EXPOSE 80

ENTRYPOINT dotnet run
