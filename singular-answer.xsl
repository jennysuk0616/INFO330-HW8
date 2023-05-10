<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/pokedex">
    Single type pokemon: <xsl:value-of select="count(pokemon[not(type[position() > 1])])" />:

    <xsl:apply-templates select="pokemon[not(type[position() > 1])]"/>
</xsl:template>

<xsl:template match="pokemon">
    <xsl:value-of select="name" /> (<xsl:value-of select="pokedexNumber" />): <xsl:value-of select="classification" /> | <xsl:apply-templates select="type"/>
</xsl:template>
