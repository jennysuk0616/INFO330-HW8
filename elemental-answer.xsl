<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/pokedex">
  <xsl:variable name="pokemonResults" select="pokemon[type = 'fire' or type = 'water' or type = 'flying' or type = 'ground']" />

  <html>
    <body>
      <h2>Elemental Pokemon</h2>
      A total of <xsl:value-of select="count($pokemonResults)" />:
      <table border="1">
        <tr bgcolor="#9acd32">
          <th>Name (Pokedex Number)</th>
          <th>Type(s)</th>
        </tr>
        <xsl:apply-templates select="$pokemonResults" />
      </table>
    </body>
  </html>
</xsl:template>

<xsl:template match="pokemon">
  <tr>
    <td><xsl:value-of select="name" />(<xsl:value-of select="@pokedex" />)</td>
    <td>
      <xsl:apply-templates select="type[position() != last()]" />
      <xsl:apply-templates select="type[position() = last()]" />
    </td>
  </tr>
</xsl:template>

<xsl:template match="type[position() != last()]">
  <xsl:value-of select="text()" />, 
</xsl:template>

<xsl:template match="type[position() = last()]">
  <xsl:value-of select="text()" />
</xsl:template>

