<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/pokedex">
    <xsl:apply-templates select="pokemon[@generation = '1']" />
</xsl:template>

<xsl:template match="pokemon">
    <xsl:value-of select="name" /> (<xsl:value-of select="@pokedex" />): <xsl:value-of select="generation" /> | 
</xsl:template>

